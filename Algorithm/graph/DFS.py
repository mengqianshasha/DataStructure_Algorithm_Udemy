class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


# Iteration version of DFS with stack
def depth_first_search(start_node):

    stack = [start_node]

    while stack:
        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)

        for node in actual_node.adjacency_list[::-1]:
            if not node.visited:
                stack.append(node)

# recursion version of DFS
# def depth_first_search(node):
#     if not node.visited:
#         print(node.name)
#         node.visited = True
#
#         for n in node.adjacency_list:
#             depth_first_search(n)


if __name__ == '__main__':
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    node6 = Node('F')
    node7 = Node('G')

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node1.adjacency_list.append(node4)
    node2.adjacency_list.append(node5)
    node2.adjacency_list.append(node6)
    node6.adjacency_list.append(node7)

    depth_first_search(node1)