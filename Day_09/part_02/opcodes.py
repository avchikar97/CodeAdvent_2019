import os
import math
from typing import IO

class IntcodeComputer:

    def __init__(self, intcodes: list, phase_setting: int):
        self.intcodes = intcodes
        self.phase_setting = phase_setting
        self.current_address = 0
        self.choose_input = 0
        self.return_list = []

    def doShit(self, input_num: int, DEBUG: int = 0):
        if(DEBUG):
            print(f"Input = {input_num}, phase setting = {self.phase_setting}")
        numbers = self.intcodes
        while self.current_address < len(numbers):
            opcode = (numbers[self.current_address] % 100) # ones and tenths place
            instruction_digits = [int(y) for y in str(numbers[self.current_address])]
            if(len(instruction_digits) != 0):
                instruction_digits.pop() # don't care
            if(len(instruction_digits) != 0):
                instruction_digits.pop() # don't care
            instruction_digits.reverse()

            if (opcode == 1) or (opcode == 2):
                modes = [0, 0, 0]
                args = [numbers[self.current_address+1], numbers[self.current_address+2], numbers[self.current_address+3]]
                badbad = False
                for idx, instruction_digit in enumerate(instruction_digits):
                    modes[idx] = instruction_digit # e.g. modes[0] is the mode of the first parameter
                for idx, mode in enumerate(modes):
                    if(mode == 0):
                        if(args[idx] > len(numbers)):
                            badbad = True
                            continue
                        args[idx] = numbers[args[idx]] # get the number at this address (taken as address)
                    else:
                        args[idx] = args[idx] # take it as a value
                if(badbad):
                    break
                if(opcode == 1):
                    numbers[numbers[self.current_address+3]] = args[1] + args[0]
                elif(opcode == 2):
                    numbers[numbers[self.current_address+3]] = args[1] * args[0]
                self.current_address += 4
            elif (opcode == 3):
                input_value = 0
                if(self.choose_input == 0):
                    input_value = self.phase_setting
                    self.choose_input = 1
                else:
                    input_value = input_num
                pos1 = numbers[self.current_address+1]
                if(pos1 > len(numbers)):
                    break
                numbers[pos1] = input_value
                self.current_address += 2
            elif (opcode == 4):
                pos1 = numbers[self.current_address+1]
                if(pos1 > len(numbers)):
                    break
                self.return_list.append(numbers[pos1])
                self.current_address += 2
                return self.return_list
            elif(opcode == 5):
                modes = [0, 0]
                args = [numbers[self.current_address+1], numbers[self.current_address+2]]
                badbad = False
                for idx, instruction_digit in enumerate(instruction_digits):
                    modes[idx] = instruction_digit # e.g. modes[0] is the mode of the first parameter
                for idx, mode in enumerate(modes):
                    if(mode == 0):
                        if(args[idx] > len(numbers)):
                            badbad = True
                            continue
                        args[idx] = numbers[args[idx]] # get the number at this address (taken as address)
                    else:
                        args[idx] = args[idx] # take it as a value
                if(badbad):
                    break
                if(args[0] != 0):
                    self.current_address = args[1]
                else:
                    self.current_address += 3
            elif(opcode == 6):
                modes = [0, 0]
                args = [numbers[self.current_address+1], numbers[self.current_address+2]]
                badbad = False
                for idx, instruction_digit in enumerate(instruction_digits):
                    modes[idx] = instruction_digit # e.g. modes[0] is the mode of the first parameter
                for idx, mode in enumerate(modes):
                    if(mode == 0):
                        if(args[idx] > len(numbers)):
                            badbad = True
                            continue
                        args[idx] = numbers[args[idx]] # get the number at this address (taken as address)
                    else:
                        args[idx] = args[idx] # take it as a value
                if(badbad):
                    break
                if(args[0] == 0):
                    self.current_address = args[1]
                else:
                    self.current_address += 3
            elif(opcode == 7):
                modes = [0, 0, 0]
                args = [numbers[self.current_address+1], numbers[self.current_address+2], numbers[self.current_address+3]]
                badbad = False
                for idx, instruction_digit in enumerate(instruction_digits):
                    modes[idx] = instruction_digit # e.g. modes[0] is the mode of the first parameter
                for idx, mode in enumerate(modes):
                    if(mode == 0):
                        if(args[idx] > len(numbers)):
                            badbad = True
                            continue
                        args[idx] = numbers[args[idx]] # get the number at this address (taken as address)
                    else:
                        args[idx] = args[idx] # take it as a value
                if(badbad):
                    break
                if(args[0] < args[1]):
                    numbers[numbers[self.current_address+3]] = 1
                else:
                    numbers[numbers[self.current_address+3]] = 0
                self.current_address += 4
            elif(opcode == 8):
                modes = [0, 0, 0]
                args = [numbers[self.current_address+1], numbers[self.current_address+2], numbers[self.current_address+3]]
                badbad = False
                for idx, instruction_digit in enumerate(instruction_digits):
                    modes[idx] = instruction_digit # e.g. modes[0] is the mode of the first parameter
                for idx, mode in enumerate(modes):
                    if(mode == 0):
                        if(args[idx] > len(numbers)):
                            badbad = True
                            continue
                        args[idx] = numbers[args[idx]] # get the number at this address (taken as address)
                    else:
                        args[idx] = args[idx] # take it as a value
                if(badbad):
                    break
                if(args[0] == args[1]):
                    numbers[numbers[self.current_address+3]] = 1
                else:
                    numbers[numbers[self.current_address+3]] = 0
                self.current_address += 4
            elif opcode == 99:
                return 99
            else:
                continue
        return 99
