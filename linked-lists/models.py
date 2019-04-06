class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        # this method pushes a new node in the beginning of the list
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
