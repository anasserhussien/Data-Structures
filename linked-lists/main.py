from models import Node, LinkedList

list_root = LinkedList()
list_root.head = Node(1)

second = Node(2)
third = Node(3)

list_root.head.next = second
second.next = third

list_root = list_root.head

while list_root:
    print(list_root.data)
    list_root = list_root.next

'''
            Visualization to the current state
     So all three nodes are linked.

    list_root.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +---
'''


'''
So Linked list provides the following two advantages over arrays
1) Dynamic size
2) Ease of insertion/deletion

Linked lists have following drawbacks:
1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do a binary search with linked lists.
2) Extra memory space for a pointer is required with each element of the list.
3) Arrays have better cache locality that can make a pretty big difference in performance.
'''
