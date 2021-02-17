class DijkstraAlgorithm:
    def __init__(self, matrix, start_vertex):
        # Not sure if self.xxx can be used in __init__ method
        # Vertices are represented by the index of the matrix
        self.matrix = matrix
        self.start_vertex = start_vertex
        self.v = len(self.matrix)
        self.min_distance = [float('inf') for _ in range(self.v)]
        self.visited = [False for _ in range(self.v)]

    # find the vertex that has the minimum value
    def __find_min__(self):
        min_distance = float('inf')
        min_index = 0

        for index in range(self.v):
            if not self.visited[index] and self.min_distance[index] < min_distance:
                min_index = index
                min_distance = self.min_distance[index]

        return min_index

    def calculate(self):
        # The min_distance of start_vertex is 0
        self.min_distance[self.start_vertex] = 0

        # Find the min_value of all vertices
        # Update it's adjacent vertices' value if found smaller
        # Involves 2 loops: O(v^2)
        for item in range(self.v):
            min_index = self.__find_min__()
            self.visited[min_index] = True
            print(f'Considering vertex {min_index}')

            for others in range(self.v):
                weight = self.matrix[min_index][others]
                if not self.visited[others] and weight:
                    new_distance = self.min_distance[min_index] + weight
                    if new_distance < self.min_distance[others]:
                        self.min_distance[others] = new_distance

    def print_distance(self):
        print(self.min_distance)


if __name__ == '__main__':
    m = [[0, 7, 5, 2, 0, 0],
         [7, 0, 0, 0, 3, 8],
         [5, 0, 0, 10, 4, 0],
         [2, 0, 10, 0, 0, 2],
         [0, 3, 4, 0, 0, 6],
         [0, 8, 0, 2, 6, 0]]

    algorithm = DijkstraAlgorithm(m, 0)
    algorithm.calculate()
    algorithm.print_distance()

