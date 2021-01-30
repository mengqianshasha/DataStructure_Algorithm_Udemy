from collections import deque

class MazeSolver():
    def __init__(self, matrix):
        self.matrix = matrix
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, -1, 1]
        self.visited = [[False for _ in range(len(self.matrix))] for _ in range(len(self.matrix))]
        self.min_dist = float('inf')

    def _is_valid(self, x, y):
        if x < 0 or x >= len(self.matrix) or y < 0 or y >= len(self.matrix):
            return False
        elif self.matrix[y][x] == 0:
            return False
        elif self.visited[y][x]:
            return False
        return True

    def _is_destination(self, x, y, x_destination, y_destination):
        if x == x_destination and y == y_destination:
            return True
        return False

    def search(self, x, y, x_destination, y_destination):
        queue = deque()
        queue.append((x, y, 0))
        self.visited[y][x] = True

        while queue:
            i, j, dist = queue.popleft()
            if self._is_destination(i, j, x_destination, y_destination):
                self.min_dist = dist
                break

            for num in range(len(self.x_move)):
                i_next = i + self.x_move[num]
                j_next = j + self.y_move[num]

                if self._is_valid(i_next, j_next):
                    queue.append((i_next, j_next, dist + 1))
                    self.visited[j_next][i_next] = True

    def show_result(self):
        if self.min_dist == float('inf'):
            print('The destination cannot be reached')
        else:
            print(f'The shortest path from source to destination: {self.min_dist}')


if __name__=='__main__':

    m = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    maze_solver = MazeSolver(m)
    maze_solver.search(0, 0, 4, 4)
    maze_solver.show_result()