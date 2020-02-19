from typing import List, Tuple
import sys
# allows me to import from graph directory
sys.path.append("../graph")
from graph import Graph

def earliest_ancestor(
    ancestors: List[Tuple[int, int]], 
    starting_node: int
):
    gr = Graph()

    geneology = dict()

    for ancestor in ancestors:
        child = ancestor[1]
        geneology[child] = list()

    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        geneology[child].append(parent)

    if starting_node not in geneology:
        raise IndexError(F"Node does not exist")
        return None
    
    print(geneology[starting_node][-1])
    return geneology[starting_node][-1]




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 2)
