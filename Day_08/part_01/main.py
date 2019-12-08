import os
from typing import IO
import time
from pathlib import Path
import numpy as np

def main():
    start_time = time.time()
    data_folder = Path(os.path.dirname(os.path.abspath(__file__)))
    input_file_path = data_folder/"input"
    width = 25
    height = 6
    with open(input_file_path, "rt") as fp:
        doShit(fp, width, height)
    print("--- %s seconds ---" % (time.time() - start_time))

def doShit(input_file: IO, width: int, height: int):
    contents = input_file.read()
    pixel_strings = list(contents)
    pixel_values = [int(element) for element in pixel_strings]
    pixel_values = [pixel_values[i:i+(width*height)] for i in range(0,len(pixel_values),width*height)]
    pixel_layers = []
    number_zero = []
    pixel_layer_counts = []
    for pixel_layer in pixel_values:
        pixel_layers.append(np.reshape(pixel_layer, (height, width)))
    for pixel_layer in pixel_layers:
        unique, counts = np.unique(pixel_layer, return_counts=True)
        abc = dict(zip(unique, counts))
        number_zero.append(abc.get(0))
        pixel_layer_counts.append(abc)
    
    answer = 1
    answer_counts = pixel_layer_counts[number_zero.index(min(number_zero))]
    print(answer_counts)

    if 1 in abc.keys():
        answer = answer*answer_counts.get(1)
    if 2 in abc.keys():
        answer = answer*answer_counts.get(2)
        
    print(answer)




if __name__ == "__main__":
    main()