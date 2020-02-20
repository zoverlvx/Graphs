
'''

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. 
The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

How can we make a graph?
    put the ancestors into a graph
    need a vertex and edge
BFS - Search for the earliest possible ancestor

'''
from stack import Stack
from typing import List, Tuple


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, child, parent):
        if child in self.vertices and parent in self.vertices:
            self.vertices[child].add(parent)

        elif child not in self.vertices and parent not in self.vertices:
            raise IndexError(f"ERR: Vertices do not exist: {child} & {parent}")
        elif child not in self.vertices:
            raise IndexError(f"ERR: That Vertex does not exist: {child}")
        elif parent not in self.vertices:
            raise IndexError(f"ERR: That Vertex does not exist: {parent}")

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

    def dfs(self, starting_vertex):

        # check and see if the vertex has a parent at all
        if len(self.get_neighbors(starting_vertex)) == 0:
            return -1

        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size() > 0:
            vert = s.pop()

            if vert not in visited:
                visited.add(vert)

                if len(self.get_neighbors(vert)) == 2:
                    parents = []

                    for neighbor in self.get_neighbors(vert):
                        parents.append(neighbor)

                    if parents[1] < parents[0]:
                        s.push(parents[1])
                        s.push(parents[0])
                    else:
                        s.push(parents[0])
                        s.push(parents[1])

                else:
                    for neighbor in self.get_neighbors(vert):
                        s.push(neighbor)
            if s.size() == 0:
                return vert


def earliest_ancestor(
    ancestors: List[Tuple[int, int]], 
    starting_node: int
) -> int:
    graph = Graph()
    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        
        # adds parent to graph
        graph.add_vertex(parent)
        # adds child to graph
        graph.add_vertex(child)
        # establishes relationship between parent and child
        graph.add_edge(child, parent)

    print(graph.vertices)
    print(graph.dfs(starting_node))
    return graph.dfs(starting_node)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)
