from collections import deque, defaultdict

class SocialNetwork:
    def __init__(self):
        # Initialize an empty network using a defaultdict of sets
        self.network = defaultdict(set)
        # Time Complexity: O(1) for initialization
        # Space Complexity: O(1) (constant space for default dict initialization)

    def add_friendship(self, person1, person2):
        """Add a bidirectional friendship between two people."""
        self.network[person1].add(person2)
        self.network[person2].add(person1)
        # Time Complexity: O(1) on average for set operations (insertion in sets is average O(1))
        # Space Complexity: O(1) for each friendship added, overall space used grows with the number of friendships

    def find_all_friends(self, person):
        """Return a set of all friends for a given person."""
        return self.network[person]
        # Time Complexity: O(1) (average case, dictionary access is O(1))
        # Space Complexity: O(F), where F is the number of friends (space needed to store the set of friends)

    def find_common_friends(self, person1, person2):
        """Find the common friends between two people."""
        friends1 = self.find_all_friends(person1)
        friends2 = self.find_all_friends(person2)
        common_friends = friends1.intersection(friends2)
        # Time Complexity: O(F1 + F2), where F1 and F2 are the number of friends of person1 and person2, respectively
        #     - Finding friends takes O(1) each, and intersection takes O(min(F1, F2))
        # Space Complexity: O(min(F1, F2)) for storing the common friends

    def find_nth_connection(self, start, end):
        """Find the nth connection (shortest path) between two people using BFS."""
        if start not in self.network or end not in self.network:
            return -1
        
        queue = deque([(start, 0)])  # Initialize BFS queue with the start person and depth 0
        visited = set()  # Set to track visited nodes
        visited.add(start)
        
        while queue:
            current, depth = queue.popleft()
            if current == end:
                return depth
            
            for friend in self.network[current]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, depth + 1))
        
        return -1
        # Time Complexity: O(V + E), where V is the number of vertices (people) and E is the number of edges (friendships)
        #     - BFS explores each vertex and edge once
        # Space Complexity: O(V) for storing the visited set and the BFS queue

# Example usage
if __name__ == "__main__":
    sn = SocialNetwork()
    
    # Add friendships
    sn.add_friendship('Alice', 'Bob')
    sn.add_friendship('Bob', 'Janice')
    sn.add_friendship('Janice', 'Dave')
    
    # Find all friends
    print(f"Alice's friends: {sn.find_all_friends('Alice')}")
    print(f"Bob's friends: {sn.find_all_friends('Bob')}")
    
    # Find common friends
    print(f"Common friends of Alice and Bob: {sn.find_common_friends('Alice', 'Bob')}")
    
    # Find nth connection
    print(f"Connection between Alice and Janice: {sn.find_nth_connection('Alice', 'Janice')}")
    print(f"Connection between Alice and Bob: {sn.find_nth_connection('Alice', 'Bob')}")
    print(f"Connection between Alice and Dave: {sn.find_nth_connection('Alice', 'Dave')}")
