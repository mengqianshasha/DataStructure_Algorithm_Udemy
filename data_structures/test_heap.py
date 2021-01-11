import unittest
from heap import MaxHeap


class HeapTestCase(unittest.TestCase):
    def test_heapify(self):
        heap = MaxHeap()
        my_list = [4,2,6,3,8,5,23,76,4,876,34,2,5,6]
        heap.heapify(my_list)
        self.assertEqual(876, heap.pop_max())

    def test_sort(self):
        heap = MaxHeap()
        my_list = [4, 2, 6, 3, 8, 5, 23, 76, 4, 876, 34, 2, 5, 6]
        sorted_list = sorted(my_list, reverse=True)
        heap.heapify(my_list)
        heap.sort()
        self.assertEqual(sorted_list, heap.heap)


if __name__ == '__main__':
    unittest.main()
