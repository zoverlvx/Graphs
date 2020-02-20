"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("WARNING: That vertex already exists.")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create an empty queue
        q = Queue()

        # add the starting vertex_id to the queue
        q.enqueue(starting_vertex)

        # create an empty set to store visited nodes
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            
            # dequeue the first vertex
            v = q.dequeue()
            
            # check if it's been visited
            # if it hasn't been visited

            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)

                # then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # create an empty stack
        s = Stack()

        # push the starting vertex_id to the stack
        s.push(starting_vertex)

        # create an empty set to store visited nodes
        visited = set()

        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()

            # check if it's been visited
            # if it has not been visited

            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)
                # then push all neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check if the node is visited
        if visited is None:
            visited = set()

        # if not
        if starting_vertex not in visited:
            # mark it as visited
            visited.add(starting_vertex)
            print(starting_vertex)

            # call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # create an empty queue
        q = Queue()

        # add a path to the starting vertex id to the queue
        q.enqueue([starting_vertex])

        # create an empty set to store visited nodes
        visited = set()

        # while the queue is not empty
        while q.size() > 0:

            # dequeue the first path
            path = q.dequeue()

            # grab the last vertex from the path
            vertex = path[-1]

            # check if it's the target
            if vertex == destination_vertex:
                # if so, return the path
                return path

            # check if it's been visited
            if vertex not in visited:
                # if it hasn't been visited
                # mark as visited
                visited.add(vertex)
                # then add a path to all neighbors to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    # make a copy of the path before adding
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # create an empty stack
        stack = Stack()

        # add a path to the starting vertex id to the stack
        stack.push([starting_vertex])

        # create an empty set to store visited nodes
        visited = set()


        while stack.size() > 0:

            path = stack.pop()
            # grab the last vertex from the path
            vertex = path[-1]

            # check if it's the target
            if vertex == destination_vertex:
                # if so, return the path
                return path

            # check if it's been visited

            if vertex not in visited:
                # if it hasn't been visited
                # mark as visited
                visited.add(vertex)
                # then add a path to all neighbors to the top of the stack
                for neighbor in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize visited if not already
        if visited is None:
            visited = set()
        # same with path
        if path is None:
            path = []

        # check if starting vertex has been visited
        if starting_vertex not in visited:
            # mark it as visited and add it to the path
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)

            # if the starting vertex is destination
            if starting_vertex == target_value:
                return path_copy
            
            # call dfs recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, target_value,
                visited, path_copy)
                if new_path is not None:
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
