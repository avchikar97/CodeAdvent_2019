import os
import math
from typing import IO

def main():
    input_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\\input"
    with open(input_file_path, "rt") as fp:
        doShit(fp)

def doShit(input_file: IO):
    contents = input_file.read()
    x = contents.split(",")
    numbers = [int(element) for element in x]
    i = 0
    while i < len(x):
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
        if (opcode == 3):
            input_value = int(input("Enter input: "))
            pos1 = numbers[i+1]
            if(pos1 > len(numbers)):
                break
            numbers[pos1] = input_value
            i += 2
        if (opcode == 4):
            pos1 = numbers[i+1]
            if(pos1 > len(numbers)):
                break
            print(numbers[pos1])
            i += 2
        elif opcode == 99:
            break
    print(f"First number = {numbers[0]}")


if __name__ == "__main__":
    main()