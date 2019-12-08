import os
import math
from typing import IO
import numpy as np
import time

SOME_SIZE = 30000
CENTER = SOME_SIZE/2

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def main():
    start_time = time.time()
    input_file_path = f"{os.path.dirname(os.path.abspath(__file__))}/input"
    with open(input_file_path, "rt") as fp:
        lines = fp.read().split("\n")
        doStuff(lines)
    print("--- %s seconds ---" % (time.time() - start_time))

def doStuff(lines: list):
    center = [CENTER, CENTER]
    curr = [CENTER, CENTER]
    grid = np.full((SOME_SIZE, SOME_SIZE), 1)
    directions = []
    intersection_number = 1
    for index in range(0, len(lines)):
        intersection_number *= primes[index]
    for (index, line) in enumerate(lines):
        directions.append(line.split(","))
    for (idx_direction, commands) in enumerate(directions):
        this_prime = primes[idx_direction]
        curr = [CENTER, CENTER]
        for(idx_directive, command) in enumerate(commands):
            direction = command[0]
            distance = int(command[1:])
            direction_modifier = -2
            direction_index = -2
            if(direction == "U"):
                direction_index = 0
                direction_modifier = -1
            elif(direction == "D"):
                direction_index = 0
                direction_modifier = 1
            elif(direction == "L"):
                direction_index = 1
                direction_modifier = -1
            elif(direction == "R"):
                direction_index = 1
                direction_modifier = 1
            else:
                direction_modifier = -2
                direction_index = -2
            if(direction_index != -2):
                for j in range(0, distance):
                    curr[direction_index] += direction_modifier
                    grid[int(curr[0]), int(curr[1])] *= this_prime
    rows, cols = np.where((grid%intersection_number == 0))

    manhattan_distances = []
    intersection_coords = []
    for idx in range(0, len(rows)):
        coord = [rows[idx], cols[idx]]
        distance = ManhattanDistance(center, coord)
        manhattan_distances.append(distance)
        intersection_coords.append(coord)

        print(f"distance = {distance}, coord = {coord}, value = {grid[coord[0], coord[1]]}")

    if(len(manhattan_distances) > 0):
        shortest_distance_idx = manhattan_distances.index(min(manhattan_distances))
        print(f"Shortest distance = {manhattan_distances[shortest_distance_idx]}")
        print(f"Coordinates = {intersection_coords[shortest_distance_idx]}")
    else:
        print("There are no intersections")
        quit()

def ManhattanDistance(center, intersection):
    distance = math.sqrt(math.pow(center[0] - intersection[0], 2)) + math.sqrt(math.pow(center[1] - intersection[1], 2))
    return distance



if __name__ == "__main__":
    main()