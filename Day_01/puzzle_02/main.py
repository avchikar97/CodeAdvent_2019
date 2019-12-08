import os
import math
import time
from pathlib import Path

def main():
    start_time = time.time()
    data_folder = Path(os.path.dirname(os.path.abspath(__file__)))
    input_file_path = data_folder/"input"
    with open(input_file_path) as fp:
        total_fuel_mass = calculateTotalFuel(fp)
        print(total_fuel_mass)
    print("--- %s seconds ---" % (time.time() - start_time))

def calculateTotalFuel(input_file):
    mass = input_file.readline()
    total_fuel_mass = 0
    while mass:
        total_fuel_mass += calculateFuel(int(mass))
        mass = input_file.readline()

    return total_fuel_mass

def calculateFuel(mass : int):
    ret_value = 0
    fuel = ((math.trunc(mass/3))-2)
    while(fuel > 0):
        ret_value += fuel
        fuel = ((math.trunc(fuel/3))-2) 
    return ret_value

if __name__ == "__main__":
    main()