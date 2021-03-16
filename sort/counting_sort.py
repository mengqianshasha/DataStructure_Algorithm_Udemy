import random

class CountingSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        max_val = max(self.arr)
        min_val = min(self.arr)
        diff = max_val - min_val + 1

        # Establishing a counting array the size of which is the difference
        counting_arr = [0] * diff

        # Increment the counting array's value if the index key is encountered in the original array
        for i in range(len(self.arr)):
            counting_arr[self.arr[i] - min_val] += 1

        # Start to sort in the original array
        k = 0
        for i in range(diff):
            while counting_arr[i] > 0:
                self.arr[k] = i + min_val
                counting_arr[i] -= 1
                k += 1

if __name__ == "__main__":
    arr = [20, 92, 7, 42, 57, 30, 28,28,28, 95]
    counting_sort = CountingSort(arr)
    counting_sort.sort()
    print(arr)



