import os
from typing import IO
from anytree import Node
import opcodes
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
    amp_permutations = itertools.permutations([0, 1, 2, 3, 4])
    phase_permutations = []
    outputs = []
    DEBUG_VALUE = 0
    for amp_perm in amp_permutations :
        input_set = [0]
        for setting in amp_perm:
            amp_output = opcodes.doShit(deepcopy(operations), input_set[-1], setting, DEBUG_VALUE)
            input_set.append(amp_output[-1])
        outputs.append(input_set[-1])
        phase_permutations.append(amp_perm)
        if(DEBUG_VALUE):
            print(f"Phase settings = {amp_perm}, I/O = {input_set}")
    maxpos = outputs.index(max(outputs))
    print(f"Max number = {outputs[maxpos]} with phase settings = {phase_permutations[maxpos]}")




if __name__ == "__main__":
    main()