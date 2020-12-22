class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data}'


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        if self.head is None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def add_to_start(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        if self.head is None:
            self.tail = x
        else:
            x.next = self.head
        self.head = x

    # search value x, return index
    def search_val(self, x):
        curr = self.head
        index = 0
        while curr:
            if curr.data == x:
                return index
            else:
                curr = curr.next
                index += 1
        return None

    # return the value of index-x Node
    def remove_val_by_index(self, x):
        length = self.length()
        if self.length() == 0:
            return None
        elif self.length() == 1 and x == 0:
            temp = self.head
            self.head = None
            self.tail = None
            return temp.data
        elif length and x < length:
            curr = self.head
            if x == 0:
                self.head = curr.next
                val = curr.data
                curr = None
                return val
            else:
                index = 0
                while index < x-1:
                    curr = curr.next
                    index += 1
                if x == length-1:
                    self.tail = curr
                temp = curr.next
                val = temp.data
                curr.next = temp.next
                temp = None
                return val
        else:
            return None

    def length(self):
        num = 0
        curr = self.head
        while curr:
            curr = curr.next
            num += 1
        return num

    def __str__(self):
        to_print = ""
        curr = self.head
        while curr:
            to_print += str(curr.data) + '->'
            curr = curr.next
        if to_print:
            return '[' + to_print[:-2] +']'
        else:
            return '[]'

    def reverse_list_recur(self, current, previous):
        if self.head is None:
            return
        elif current.next is None:
            self.tail = self.head
            current.next = previous
            self.head = current
        else:
            temp = current.next
            current.next = previous
            self.reverse_list_recur(temp, current)






