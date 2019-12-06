import os
from typing import IO
from anytree import Node, Walker

def main():
    input_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\\input"
    with open(input_file_path, "rt") as fp:
        doShit(fp)

def doShit(input_file: IO):
    pair = input_file.readline()
    graph = dict()
    IDX_ORBITEE = 0
    IDX_ORBITER = 1
    min_transfers = 0
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
    w = Walker()
    (upwards, common, downwards) = w.walk(graph["YOU"], graph["SAN"])
    min_transfers = len(upwards) + len(downwards) - 2 # don't need to count the initial thing and the final thing

    print(f"Number of minimum transfers: {min_transfers}")



if __name__ == "__main__":
    main()