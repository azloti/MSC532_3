import hashlib

def stable_hash(x):
    return int(hashlib.md5(x.encode('utf8')).hexdigest(),16)

# A Node class to represent the elements in the hash table
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    # Constructor to initialize the hash table with a fixed size
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # A simple hash function to calculate the index of the key
    def hash_for_key(self, key):
        # Keep in mind python's hash function returns different values for different runs
        return stable_hash(key) % self.size

    # Insert a key-value pair into the hash table
    def insert(self, key, value):

        # Calculate the index of the key
        index = self.hash_for_key(key)
        print(f'Adding {key}: {value} at index {index}')
        if self.table[index] is None:
            # If the index is empty, create a new node
            self.table[index] = Node(key, value)
        else:
            # If the index is not empty, add the new node at the start of the chain in O(1) time complexity
            node = Node(key, value)
            node.next = self.table[index]
            self.table[index] = node

    def get(self, key):
        # Get the node at the index of the key
        current_node = self.table[self.hash_for_key(key)]

        # Traverse the chain to find the key
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next

        # If the key is not found, return None
        return None

    def delete(self, key):
        # Calculate the index of the key
        index = self.hash_for_key(key)

        # Get the node at the index of the key
        current_node = self.table[index]
        prev = None
        while current_node is not None:
            if current_node.key == key:
                if prev is None:
                    self.table[index] = current_node.next
                else:
                    prev.next = current_node.next
                return
            prev = current_node
            current_node = current_node.next

    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            current_node = self.table[i]
            while current_node is not None:
                print(f"({current_node.key}, {current_node.value})", end=" -> ")
                current_node = current_node.next
            print("None")

# Example usage
hash_table = HashTable(10)
hash_table.insert("nichita", "CS")
hash_table.insert("diana", "Law")
hash_table.insert("cristi", "Management")
hash_table.insert("nastia", "Math")

hash_table.display()