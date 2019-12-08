import os
import math
import time

def main():
    start_time = time.time()
    input_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\\input"
    with open(input_file_path) as fp:
        total_fuel_mass = calculateAllMasses(fp)
        print(total_fuel_mass)
    print("--- %s seconds ---" % (time.time() - start_time))

def calculateAllMasses(input_file):
    mass = input_file.readline()
    total_fuel_mass = 0
    while mass:
        total_fuel_mass += calculateMass(mass)
        mass = input_file.readline()

    return total_fuel_mass

def calculateMass(mass):
    return ((math.trunc(int(mass)/3))-2)

if __name__ == "__main__":
    main()