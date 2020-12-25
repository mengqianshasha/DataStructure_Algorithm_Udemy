class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root is None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data < curr.data:
            if curr.left is None:
                curr.left = key
            else:
                self._insert(curr.left, key)
        elif key.data > curr. data:
            if curr.right is None:
                curr.right = key
            else: self._insert(curr.right, key)

    def in_order(self):
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left)
            print(curr.data, end=" ")
            self._in_order(curr.right)

    def pre_order(self):
        self._pre_order(self.root)
        print("")

    def _pre_order(self, curr):
        if curr:
            print(curr.data, end=" ")
            self._pre_order(curr.left)
            self._pre_order(curr.right)

    def post_order(self):
        self._post_order(self.root)
        print("")

    def _post_order(self, curr):
        if curr:
            self._post_order(curr.left)
            self._post_order(curr.right)
            print(curr.data, end=" ")

    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return "Node is found in the tree."
            elif key < curr.data:
                return self._find_val(curr.left, key)
            elif key > curr.data:
                return self._find_val(curr.right, key)
        return "Not exist."

    def min_right_subtree(self, curr):
        if curr.left == None:
            return curr
        else:
            return self.min_right_subtree(curr.left)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                # 1. There is parent, with no child
                if curr.left is None and curr.right is None:
                    if prev:
                        if is_left:
                            prev.left = None
                        else:
                            prev.right = None
                    else:
                        self.root = None
                # 2. There is right child
                elif curr.left is None:
                    if prev:
                        if is_left:
                            prev.left = curr.right
                        else:
                            prev.right = curr.right
                    else:
                        self.root = curr.right
                # 3. There is left child
                elif curr.right is None:
                    if prev:
                        if is_left:
                            prev.left = curr.left
                        else:
                            prev.right = curr.left
                    else:
                        self.root = curr.left
                # 4. There are both children
                else:
                    min_child = self.min_right_subtree(curr.right)
                    curr.data = min_child.data
                    self._delete_val(curr.right, curr, False, min_child.data)

            elif key < curr.data:
                self._delete_val(curr.left, curr, True, key)
            elif key > curr.data:
                self._delete_val(curr.right, curr, False, key)

        else:
            print(f"{key} not found in tree")

