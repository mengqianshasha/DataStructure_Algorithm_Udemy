import unittest
from linked_list import *


class LinkedListTestCase(unittest.TestCase):
    def test_append_val(self):
        my_list = LinkedList()
        my_list.append_val(3)
        self.assertEqual(3, my_list.head.data)
        self.assertEqual(3, my_list.tail.data)

        my_list = self.__default_linkedlist__()
        self.assertEqual(0, my_list.head.data)
        self.assertEqual(9, my_list.tail.data)

    def test_add_to_start(self):
        my_list = LinkedList()
        my_list.add_to_start(3)
        self.assertTrue(3, my_list.head.data)
        self.assertTrue(3, my_list.tail.data)

        default_list = self.__default_linkedlist__()
        my_list = LinkedList()
        for n in range(10):
            my_list.add_to_start(n)
        self.assertEqual(default_list.head.data, my_list.tail.data)
        self.assertEqual(default_list.tail.data, my_list.head.data)

    def test_search_val(self):
        my_list = self.__default_linkedlist__()
        index = my_list.search_val(5)
        self.assertEqual(5, index)

    def test_length(self):
        my_list = self.__default_linkedlist__()
        self.assertEqual(10, my_list.length())

    def test_remove(self):
        my_list = self.__default_linkedlist__()
        my_list.remove_val_by_index(9)
        self.assertEqual(8, my_list.tail.data)
        my_list.remove_val_by_index(0)
        self.assertEqual(1, my_list.head.data)
        self.assertEqual(6, my_list.remove_val_by_index(5))

        my_list = LinkedList()
        my_list.append_val(3)
        self.assertEqual(3, my_list.remove_val_by_index(0))
        self.assertEqual(None, my_list.head)
        self.assertEqual(None, my_list.tail)

    def test_reverse(self):
        my_list = self.__default_linkedlist__()
        my_list.reverse_list_recur(my_list.head, None)
        self.assertEqual(9, my_list.head.data)
        self.assertEqual(0, my_list.tail.data)
        print(my_list)

    def __default_linkedlist__(self):
        my_list = LinkedList()
        for n in range(10):
            my_list.append_val(n)
        return my_list


if __name__ == '__main__':
    unittest.main()

