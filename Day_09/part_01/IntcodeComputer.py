import numpy as np

class IntcodeComputer:

    def __init__(self, intcodes: list):
        self.intcodes = intcodes
        self.current_address = 0
        self.return_list = []
        self.relative_base = 0
        self.address_increment_dict = {
            1: 4,
            2: 4,
            3: 2,
            4: 2,
            5: 3,
            6: 3,
            7: 4,
            8: 4,
            9: 2
        }

    def processModes(self, operations: list, modes: list, args: list):
        for idx in range(0, len(args)):
            if(modes[idx] == 0): # 0: position mode
                if(args[idx] > len(operations)):
                    operations.extend(np.zeros((args[idx] + 2) - len(operations), dtype=int))
                args[idx] = operations[args[idx]] # get the number at this address (taken as address)
            elif(modes[idx] == 2): # 2: relative mode
                if((self.relative_base + args[idx]) > len(operations)):
                    operations.extend(np.zeros((self.relative_base + args[idx] + 1) - len(operations), dtype=int))
                args[idx] = operations[self.relative_base + args[idx]] # get the number at this address (taken as address)
            else:
                args[idx] = args[idx] # 1: value mode
        return

    def doShit(self, input_num: int, DEBUG: int = 0):
        numbers = self.intcodes
        while self.current_address < len(numbers):
            opcode = (numbers[self.current_address] % 100) # ones and tenths place
            instruction_digits = [int(y) for y in str(numbers[self.current_address])]
            if(len(instruction_digits) != 0):
                instruction_digits.pop() # don't care
            if(len(instruction_digits) != 0):
                instruction_digits.pop() # don't care
            instruction_digits.reverse()
            modes = [0, 0, 0]
            for idx, instruction_digit in enumerate(instruction_digits):
                modes[idx] = instruction_digit # e.g. modes[0] is the mode of the first parameter

            if (opcode == 1):
                args = [numbers[self.current_address+1], numbers[self.current_address+2], numbers[self.current_address+3]]
                self.processModes(numbers, modes, args)
                numbers[numbers[self.current_address+3]] = args[1] + args[0]
                self.current_address += self.address_increment_dict.get(opcode)
            elif (opcode == 2):
                args = [numbers[self.current_address+1], numbers[self.current_address+2], numbers[self.current_address+3]]
                self.processModes(numbers, modes, args)
                numbers[numbers[self.current_address+3]] = args[1] * args[0]
                self.current_address += self.address_increment_dict.get(opcode)
            elif (opcode == 3):
                input_value = input_num
                args = [numbers[self.current_address+1]]
                self.processModes(numbers, modes, args)
                numbers[args[0]] = input_value
                self.current_address += self.address_increment_dict.get(opcode)
            elif (opcode == 4):
                args = [numbers[self.current_address+1]]
                self.processModes(numbers, modes, args)
                self.return_list.append(args[0])
                self.current_address += self.address_increment_dict.get(opcode)
                return self.return_list
            elif (opcode == 5):
                args = [numbers[self.current_address+1], numbers[self.current_address+2]]
                self.processModes(numbers, modes, args)
                if(args[0] != 0):
                    self.current_address = args[1]
                else:
                    self.current_address += self.address_increment_dict.get(opcode)
            elif (opcode == 6):
                args = [numbers[self.current_address+1], numbers[self.current_address+2]]
                self.processModes(numbers, modes, args)
                if(args[0] == 0):
                    self.current_address = args[1]
                else:
                    self.current_address += self.address_increment_dict.get(opcode)
            elif (opcode == 7):
                args = [numbers[self.current_address+1], numbers[self.current_address+2], numbers[self.current_address+3]]
                self.processModes(numbers, modes, args)
                if(args[0] < args[1]):
                    numbers[numbers[self.current_address+3]] = 1
                else:
                    numbers[numbers[self.current_address+3]] = 0
                self.current_address += self.address_increment_dict.get(opcode)
            elif (opcode == 8):
                args = [numbers[self.current_address+1], numbers[self.current_address+2], numbers[self.current_address+3]]
                self.processModes(numbers, modes, args)
                if(args[0] == args[1]):
                    numbers[numbers[self.current_address+3]] = 1
                else:
                    numbers[numbers[self.current_address+3]] = 0
                self.current_address += self.address_increment_dict.get(opcode)
            elif (opcode == 9):
                args = [numbers[self.current_address+1]]
                self.processModes(numbers, modes, args)
                self.relative_base += args[0]
                self.current_address += self.address_increment_dict.get(opcode)
            elif (opcode == 99):
                return 99
            else:
                continue
        return 99
