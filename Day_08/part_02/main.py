import os
from typing import IO
import time
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

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
    for pixel_layer in pixel_values:
        pixel_layers.append(np.reshape(pixel_layer, (height, width)))
    
    final_answer = np.zeros((height, width))
    for i in range(0, width):
        for j in range(0, height):
            for layer in pixel_layers:
                if(layer[j, i] == 2):
                    continue
                else:
                    final_answer[j, i] = layer[j, i]
                    break

    print(final_answer)

    plt.imshow(final_answer) # display answer

    plt.show()


if __name__ == "__main__":
    main()