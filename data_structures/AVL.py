class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1


class AVLTree:

    def insert(self, data, node):
        # normal BST insertion
        if not node:
            return Node(data)
        elif data < node.data:
            node.left = self.insert(data, node.left)
        else:
            node.right = self.insert(data, node.right)

        # update height of parent node
        node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1

        # get the balance factor
        balance = self.balance_factor(node)

        # rotate if unbalanced with 4 possible scenarios
        # 1. left left
        if balance > 1 and data < node.left.data:
            return self.right_rotate(node)
        #2. left right
        if balance > 1 and data < node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        #3. right right
        if balance < -1 and data > node.right.data:
            return self.left_rotate(node)
        #4. right left
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # return the node if balanced
        return node

    def calculate_height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.calculate_height(node.left) - self.calculate_height(node.right)

    def left_rotate(self, z):
        # refer to right right case pic
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = max(self.calculate_height(z.left), self.calculate_height(z.right)) + 1
        y.height = max(self.calculate_height(y.left), self.calculate_height(y.right)) + 1

        return y

    def right_rotate(self, z):
        # refer to left left case pic
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = max(self.calculate_height(z.left), self.calculate_height(z.right)) + 1
        y.height = max(self.calculate_height(y.left), self.calculate_height(y.right)) + 1

        return y

    def delete(self, node, data):
        # standard BST deletion
        if node is None:
            return None
        elif data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if node.right and not node.left:
                temp = node.right
                node = None
                return temp
            elif node.left and not node.right:
                temp = node.left
                node = None
                return temp
            elif not node.left and not node.right:
                node = None
                return node
            else:
                right_min = self.get_min(node.right)
                node.data = right_min
                node.right = self.delete(node.right, right_min)
                return node

        # update the height of parent node (upward until the root)
        node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1

        # get balance factor
        balance = self.balance_factor(node)

        # rotate if unbalanced (upward until the root):
        # 1. left left
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)
        # 2. left right
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # 3. right right
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)
        # 4. right left
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # return node if balanced
        return node

    def get_min(self, node):
        if node.left is None:
            return node.data
        return self.get_min(node.left)

# tree = AVLTree()
# root = None
# root = tree.insert(5, root)
# root = tree.insert(8, root)
# root = tree.insert(3, root)
# root = tree.insert(4, root)
# root = tree.insert(1, root)
# root = tree.insert(2, root)
# root = tree.insert(10, root)
# root = tree.insert(7, root)
#
# root = tree.delete(root, 5)
# print(root.height)
