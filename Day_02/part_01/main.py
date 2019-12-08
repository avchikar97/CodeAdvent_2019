import os
import math
from typing import IO
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
    numbers = [int(element) for element in x]
    for i in range(0, len(x), 4):
        opcode = numbers[i]
        if opcode == 1:
            pos1 = numbers[i+1]
            pos2 = numbers[i+2]
            pos3 = numbers[i+3]
            numbers[pos3] = numbers[pos1] + numbers[pos2]
        elif opcode == 2:
            pos1 = numbers[i+1]
            pos2 = numbers[i+2]
            pos3 = numbers[i+3]
            numbers[pos3] = numbers[pos1] * numbers[pos2]
        elif opcode == 99:
            break
    print(numbers[0])


if __name__ == "__main__":
    main()