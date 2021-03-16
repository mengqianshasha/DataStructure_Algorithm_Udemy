# Create a single linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        """Insert a new node in a singly linked list"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # insert at the beginning
        elif location == 0:
            new_node.next = self.head
            self.head = new_node

        # insert at the end
        elif location == 1:
            self.tail.next = new_node
            self.tail = new_node

        # insert in the middle
        else:
            curr = self.head
            index = 0
            while index < location - 1:
                curr = curr.next
                index += 1
            new_node.next = curr.next
            curr.next = new_node

    def traverseSLL(self):
        """traverse a singly linked list"""
        node = self.head
        if node is None:
            print('Linked list does not exist')
        else:
            while node:
                print(node.value)
                node = node.next

    def searchSLL(self, value):
        """search in a singly linked list"""


######
node1 = Node(1)
node2 = Node(2)
singlyLinkedList = SLinkedList()

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2

singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(5, 0)
singlyLinkedList.insertSLL(6, 3)

print([node.value for node in singlyLinkedList])
singlyLinkedList.traverseSLL()

