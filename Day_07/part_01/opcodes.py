import os
import math
from typing import IO

def main():
    input_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\\input"
    with open(input_file_path, "rt") as fp:
        doShit(fp, 0, 0)

def doShit(input_op_instructions: list, input_num: int, phase_setting: int, DEBUG: int = 0):
    if(DEBUG):
        print(f"Input = {input_num}, phase setting = {phase_setting}")
    choose_input = 0
    numbers = input_op_instructions
    i = 0
    return_list = []
    while i < len(numbers):
        opcode = (numbers[i] % 100) # ones and tenths place
        instruction_digits = [int(y) for y in str(numbers[i])]
        if(len(instruction_digits) != 0):
            instruction_digits.pop() # don't care
        if(len(instruction_digits) != 0):
            instruction_digits.pop() # don't care
        instruction_digits.reverse()

        if (opcode == 1) or (opcode == 2):
            modes = [0, 0, 0]
            args = [numbers[i+1], numbers[i+2], numbers[i+3]]
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
                numbers[numbers[i+3]] = args[1] + args[0]
            elif(opcode == 2):
                numbers[numbers[i+3]] = args[1] * args[0]
            i += 4
        elif (opcode == 3):
            input_value = 0
            if(choose_input == 0):
                input_value = phase_setting
                choose_input = 1
            else:
                input_value = input_num
            pos1 = numbers[i+1]
            if(pos1 > len(numbers)):
                break
            numbers[pos1] = input_value
            i += 2
        elif (opcode == 4):
            pos1 = numbers[i+1]
            if(pos1 > len(numbers)):
                break
            return_list.append(numbers[pos1])
            i += 2
        elif(opcode == 5):
            modes = [0, 0]
            args = [numbers[i+1], numbers[i+2]]
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
                i = args[1]
            else:
                i += 3
        elif(opcode == 6):
            modes = [0, 0]
            args = [numbers[i+1], numbers[i+2]]
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
                i = args[1]
            else:
                i += 3
        elif(opcode == 7):
            modes = [0, 0, 0]
            args = [numbers[i+1], numbers[i+2], numbers[i+3]]
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
                numbers[numbers[i+3]] = 1
            else:
                numbers[numbers[i+3]] = 0
            i += 4
        elif(opcode == 8):
            modes = [0, 0, 0]
            args = [numbers[i+1], numbers[i+2], numbers[i+3]]
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
                numbers[numbers[i+3]] = 1
            else:
                numbers[numbers[i+3]] = 0
            i += 4
        elif opcode == 99:
            break
        else:
            continue
    return return_list


if __name__ == "__main__":
    main()