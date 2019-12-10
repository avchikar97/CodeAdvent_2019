import os
from typing import IO
from anytree import Node
import IntcodeComputer
import itertools
from copy import deepcopy
import time
from pathlib import Path

def main():
    start_time = time.time()
    data_folder = Path(os.path.dirname(os.path.abspath(__file__)))
    input_file_path = data_folder/"input"
    with open(input_file_path, "rt") as fp:
        doShit(fp)
    print("--- %s seconds ---" % (time.time() - start_time))

def doShit(input_file: IO):
    contents = input_file.read()
    x = contents.split(",")
    operations = [int(element) for element in x]
    my_computer = IntcodeComputer.IntcodeComputer(operations)
    outputs = []
    while(True):
        output = my_computer.doShit(1)
        if(output == 99):
            break
        else:
            outputs.append(my_computer.return_list[-1])
    print(my_computer.return_list)


if __name__ == "__main__":
    main()