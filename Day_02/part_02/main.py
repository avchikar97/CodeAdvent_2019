import os
import math
from typing import IO
from copy import deepcopy
import time

def main():
    start_time = time.time()
    input_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\\input"
    with open(input_file_path, "rt") as fp:
        doShit(fp)
    print("--- %s seconds ---" % (time.time() - start_time))

def doShit(input_file: IO):
    contents = input_file.read()
    x = contents.split(",")
    number_list = [int(element) for element in x]
    for noun in range(0, 100):
        for verb in range(0, 100):
            numbers = deepcopy(number_list)
            if((noun > len(numbers)) or (verb > len(numbers)) ):
                continue
            else:
                numbers[0] = 1
                numbers[1] = noun
                numbers[2] = verb
                for i in range(0, len(x), 4):
                    opcode = numbers[i]
                    if (opcode == 1) or (opcode == 2):
                        pos1 = numbers[i+1]
                        pos2 = numbers[i+2]
                        pos3 = numbers[i+3]
                        if((pos1 > len(numbers)) or (pos2 > len(numbers)) or (pos3 > len(numbers))):
                            break
                        if(opcode == 1):
                            numbers[pos3] = numbers[pos1] + numbers[pos2]
                        elif(opcode == 2):
                            numbers[pos3] = numbers[pos1] * numbers[pos2]
                    elif opcode == 99:
                        break
                output = numbers[0]
                if output == 19690720:
                    announce(noun, verb, output)

def announce(noun, verb, output):
    print(f"noun = {noun}, verb = {verb}, answer = {100*noun + verb}")
    print(f"output = {output}")
    quit()

if __name__ == "__main__":
    main()