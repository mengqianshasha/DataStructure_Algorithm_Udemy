class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, data):
        self.heap.append(data)
        self._sift_up()
        self.size += 1

    def _sift_up(self):
        index = self.size
        index_parent = int((index - 1) / 2)

        while index_parent >= 0:
            if self.heap[index] < self.heap[index_parent]:
                break
            else:
                self.heap[index_parent], self.heap[index] = self.heap[index], self.heap[index_parent]
                index = index_parent
                index_parent = int((index - 1) / 2)

    def get_max(self):
        return self.heap[0]

    def pop_max(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_item = self.heap.pop()
        self.size -= 1
        self._sift_down(0)
        return max_item

    def _sift_down(self, index):
        index_child_left = 2 * index + 1
        index_child_right = 2 * index + 2

        while index_child_left < self.size:
            if index_child_right < self.size:
                if self.heap[index_child_left] > self.heap[index_child_right]:
                    index_larger = index_child_left
                else:
                    index_larger = index_child_right
                if self.heap[index] < self.heap[index_larger]:
                    self.heap[index], self.heap[index_larger] = self.heap[index_larger], self.heap[index]
                    index = index_larger
                    index_child_left = 2 * index + 1
                    index_child_right = 2 * index + 2
                else:
                    break
            else:
                if self.heap[index] < self.heap[index_child_left]:
                    self.heap[index], self.heap[index_child_left] = self.heap[index_child_left], self.heap[index]
                break

    def heapify(self, data_list):
        self.heap = data_list
        self.size = len(data_list)
        start_num = int(((self.size - 1) - 1) / 2)

        for i in range(start_num, -1, -1):
            self._sift_down(i)

    def sort(self):
        self.heap = [self.pop_max() for i in range(0, self.size)]