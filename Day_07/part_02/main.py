import os
from typing import IO
from anytree import Node
import opcodes
import itertools
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
    operations = [int(element) for element in x]
    amp_permutations = itertools.permutations([5, 6, 7, 8, 9])
    phase_permutations = []
    outputs = []
    DEBUG_VALUE = 0
    for amp_perm in amp_permutations :
        input_set = [0]
        amplifiers = []
        amplifier_output = 0
        for setting in amp_perm:
            amplifiers.append(opcodes.IntcodeComputer(deepcopy(operations), setting))
        amplifier_num = 0
        while(True):
            amplifier_output = amplifiers[amplifier_num].doShit(input_set[-1], DEBUG_VALUE)
            if((amplifier_output == 99) and (amplifier_num == (len(amplifiers) - 1))):
                input_set.append(amplifiers[amplifier_num].return_list[-1])
                break
            else:
                input_set.append(amplifiers[amplifier_num].return_list[-1])
            amplifier_num += 1
            amplifier_num = amplifier_num % len(amplifiers)
        outputs.append(input_set[-1])
        phase_permutations.append(amp_perm)
        if(DEBUG_VALUE):
            print(f"Phase settings = {amp_perm}, I/O = {input_set}")
    maxpos = outputs.index(max(outputs))
    print(f"Max number = {outputs[maxpos]} with phase settings = {phase_permutations[maxpos]}")




if __name__ == "__main__":
    main()