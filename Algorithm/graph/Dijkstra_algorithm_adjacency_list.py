from heapq import heappush, heappop


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.is_visited = False
        self.adjacency_list = []
        self.min_distance = float('inf')
        self.prev_vertex = None

    def __lt__(self, other):
        return self.min_distance < other.min_distance


class DijkstraAlgorithm:
    def __init__(self):
        # heap is the underlying data structure of Dijkstra's Algorithm
        self.heap = []

    def calculate(self, start_node):
        start_node.min_distance = 0
        heappush(self.heap, start_node)

        # Loop every vertex until the heap is empty
        while self.heap:
            # pop the minimum value vertex
            curr_vertex = heappop(self.heap)
            if curr_vertex.is_visited:
                continue

            # Add its next nodes to the heap if it yields minimum distance to this node.
            for edge in curr_vertex.adjacency_list:
                target_vertex = edge.target_vertex
                weight = edge.weight
                new_distance = curr_vertex.min_distance + weight
                if new_distance < target_vertex.min_distance:
                    target_vertex.min_distance = new_distance
                    target_vertex.prev_vertex = curr_vertex
                    heappush(self.heap, target_vertex)

            # Set is_visited to True after it has been popped and all its edges added.
            curr_vertex.is_visited = True

    def show_min_distance(self, node):
        print(f'The distance from source is: {node.min_distance}')
        curr_node = node
        while curr_node:
            print(curr_node.name)
            curr_node = curr_node.prev_vertex


if __name__=='__main__':
    # create the vertices (nodes)
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    # create the edges (directed edges)
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    # handle the neighbors
    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node1.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node2.adjacency_list.append(edge6)
    node8.adjacency_list.append(edge7)
    node8.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node5.adjacency_list.append(edge11)
    node6.adjacency_list.append(edge12)
    node6.adjacency_list.append(edge13)
    node3.adjacency_list.append(edge14)
    node3.adjacency_list.append(edge15)
    node4.adjacency_list.append(edge16)

    algorithm = DijkstraAlgorithm()
    algorithm.calculate(node1)
    algorithm.show_min_distance(node4)
