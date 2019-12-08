import os
from typing import IO
from anytree import Node
import time

def main():
    start_time = time.time()
    input_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\\input"
    with open(input_file_path, "rt") as fp:
        doShit(fp)
    print("--- %s seconds ---" % (time.time() - start_time))

def doShit(input_file: IO):
    pair = input_file.readline()
    graph = dict()
    IDX_ORBITEE = 0
    IDX_ORBITER = 1
    number_of_orbits = 0
    while pair: ### create all nodes
        pair = pair.replace('\n', '')
        nodes = pair.split(")")
        node_orbitee = Node(nodes[IDX_ORBITEE])
        node_orbiter = Node(nodes[IDX_ORBITER])
        graph[nodes[IDX_ORBITEE]] = node_orbitee
        graph[nodes[IDX_ORBITER]] = node_orbiter
        pair = input_file.readline()
    input_file.seek(0)
    pair = input_file.readline()
    while pair: ### build tree (assign parents)
        pair = pair.replace('\n', '')
        nodes = pair.split(")")
        graph[nodes[IDX_ORBITER]].parent = graph[nodes[IDX_ORBITEE]]
        pair = input_file.readline()
    for node in graph.values():
        number_of_orbits += node.depth

    print(f"Number of orbits: {number_of_orbits}")



if __name__ == "__main__":
    main()