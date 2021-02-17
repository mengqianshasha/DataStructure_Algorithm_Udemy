import unittest
from BST import *

class BSTTestCase(unittest.TestCase):
    def test_insert(self):
        myBST = BST()
        myBST.insert('F')
        self.assertEqual('F', myBST.root.data)

        myBST.insert('C')
        myBST.insert('G')
        myBST.insert('A')
        myBST.insert('K')
        self.assertEqual('K', myBST.root.right.right.data)

    def test_in_order(self):
        default_BST = self._default_BST()
        default_BST.in_order()

    def test_pre_order(self):
        default_BST = self._default_BST()
        default_BST.pre_order()

    def test_post_order(self):
        default_BST = self._default_BST()
        default_BST.post_order()

    def test_find_val(self):
        default_BST = self._default_BST()
        print(default_BST.find_val("F"))
        print(default_BST.find_val("Z"))
        print(default_BST.find_val("A"))

    def test_delete_val(self):
        default_BST = self._default_BST()
        default_BST.delete_val('A')
        default_BST.delete_val('G')
        default_BST.delete_val('K')
        default_BST.delete_val('H')
        default_BST.delete_val('B')
        default_BST.delete_val('F')
        default_BST.delete_val('Z')
        default_BST.in_order()


    def _default_BST(self):
        myBST = BST()
        myBST.insert('F')
        myBST.insert('C')
        myBST.insert('G')
        myBST.insert('A')
        myBST.insert('K')
        myBST.insert('H')
        myBST.insert('B')
        return myBST


if __name__ == '__main__':
    unittest.main()