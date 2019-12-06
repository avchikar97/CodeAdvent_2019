import os
import math
from typing import IO

def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            if(not node in graph.keys()):
                continue
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return 1

def main():
    input_file_path = f"{os.path.dirname(os.path.abspath(__file__))}\\input"
    with open(input_file_path, "rt") as fp:
        doShit(fp)

def doShit(input_file: IO):
    pair = input_file.readline()
    all_nodes = set()
    graph = {}
    IDX_ORBITEE = 0
    IDX_ORBITER = 1
    number_of_orbits = 0
    while pair: ### build tree
        pair = pair.replace('\n', '')
        nodes = pair.split(")")
        entry_so_far = set()
        if(nodes[IDX_ORBITEE] in graph.keys()):
            entry_so_far = graph[nodes[IDX_ORBITEE]]
            
        else:
            graph[nodes[IDX_ORBITEE]] = set()
            entry_so_far = graph[nodes[IDX_ORBITEE]]
        entry_so_far.add(str(nodes[IDX_ORBITER]))
        graph[nodes[IDX_ORBITEE]] = entry_so_far
        all_nodes.add(nodes[IDX_ORBITEE])
        all_nodes.add(nodes[IDX_ORBITER])
        pair = input_file.readline()
    #all_nodes.remove("COM")
    for node in all_nodes:
        abc = bfs_shortest_path(graph, "COM", node)
        if(abc != 1):
            number_of_orbits += len(abc)

    print(f"Number of orbits: {number_of_orbits}")



if __name__ == "__main__":
    main()