import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def get_friends(self, user_id):
        return self.friendships[user_id]

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(F"User {i+1}")

        # Create friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                friendship = (user_id, friend_id)
                possible_friendships.append(friendship)

        # shuffle the list
        random.shuffle(possible_friendships)

        # grab the first n pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        # n = avg_friendships * num_users // 2


    def populate_graph_linear(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # add users
        for i in range(num_users):
            self.add_user(F"User {i + 1}")

        friendships_to_create = avg_friendships * num_users
        friendships = 0
        collisions = 0

        # while the result of that is < the required average
        while friendships < friendships_to_create:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            # pick two users at random - if they are not already friends, make
            # them friends
            if self.add_friendship(user_id, friend_id):
                friendships += 2
            else:
                # if they are already friends, try again
                collisions += 1
        print(F"Collisions: {collisions}")


    def get_all_social_paths(self, user_id):

        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # create an empty queue
        q = Queue()

        # add a path to the starting vertex_id to the queue
        q.enqueue([user_id])

        # create an empty dict to store visited users and social paths

        visited = dict()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()

            # grab the last vertex from the path
            vertex = path[-1]

            # check if it's been visited
            if vertex not in visited:
                # if it hasn't been visited
                # mark as such
                # add it to the visited dict with the path as the value
                visited[vertex] = path

                # then add all friends to the back of the queue
                for friend_id in self.get_friends(vertex):
                    # copy the path
                    path_copy = path.copy()
                    #add friend to the path
                    path_copy.append(friend_id)
                    q.enqueue(path_copy)
        
        return visited

from time import time

if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time()
    sg.populate_graph(10, 2)
    end_time = time()
    print(F"\nQuadratic runtime: {end_time - start_time} seconds")

    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
