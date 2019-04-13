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

    def insertAfter(self, prev_node, new_data):
        # this method puts a new node after the giving node
        if prev_node is None:
            print("Prev Node doesn't exist")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        # add node in the end of the current list
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def deleteNode(self,k):

        curr_head = self.head
        _prev = curr_head
        _next = None
        if k == 1:
            self.head = self.head.next
            _prev = None
            return self.head
        while k > 1:
            _prev = curr_head
            curr_head = curr_head.next
            k-=1

        if _prev.next is None:
            _next = None
        else:
            _next = _prev.next.next
        temp = _prev.next
        _prev.next = _next
        temp = None
        return self.head

    def printAll(self):
        # print the whole list
        list_root = self.head
        while list_root:
            print(list_root.data)
            list_root = list_root.next

    def getCount(self):
        curr = self.head
        size = 0
        while curr:
            curr = curr.next
            size+=1
        return size

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
