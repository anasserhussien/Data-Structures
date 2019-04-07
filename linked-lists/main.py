from models import Node, LinkedList

list_root = LinkedList()
list_root.head = Node(1)

second = Node(2)
third = Node(3)

list_root.head.next = second
second.next = third

'''
So Linked list provides the following two advantages over arrays
1) Dynamic size
2) Ease of insertion/deletion

Linked lists have following drawbacks:
1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do a binary search with linked lists.
2) Extra memory space for a pointer is required with each element of the list.
3) Arrays have better cache locality that can make a pretty big difference in performance.
'''

llist = LinkedList()
llist.append(6)
llist.push(7);
llist.push(1);
llist.append(4)

# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
llist.insertAfter(llist.head.next, 8)

llist.printAll()
print('---------------------')
llist.deleteNode(3)
llist.printAll()
