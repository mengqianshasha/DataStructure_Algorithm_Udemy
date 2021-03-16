# List method: not in-place
def quick_sort_list(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quick_sort_list(smaller) + equal + quick_sort_list(larger)


class QuickSortLomuto:
    def __init__(self, arr):
        self.arr = arr

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def sort(self):
        self.quick_sort(0, len(self.arr) - 1)

    def quick_sort(self, low, high):
        if low >= high:
            return
        else:
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot - 1)
            self.quick_sort(pivot + 1, high)

    def partition(self, low, high):
        pivot_index = high      # choose the rightmost as pivot

        # pointer i: to track the place where smaller num should be inserted
        i = low

        # pointer j: explore nums and seek smaller nums to insert
        for j in range(low, high):
            if self.arr[j] < self.arr[pivot_index]:
                self.swap(i, j)
                i += 1

        # insert pivot in the index i spot
        self.swap(i, pivot_index)

        # return the index of the pivot
        return i


class QuickSortHoare:
    def __init__(self, arr):
        self.arr = arr

    def _swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def sort(self):
        self.quick_sort(0, len(self.arr) - 1)

    def quick_sort(self, low, high):
        if low >= high:
            return

        else:
            # pivot cannot be included in the leftside arr if choosing high as pivot
            # pivot cannot be included in the rightside arr if choosing low as pivot
            # Since the returned index is not necessarily the index of pivot, so
            #     pivot should be included in the following recursion
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot - 1)
            self.quick_sort(pivot, high)

    def partition(self, low, high):
        pivot_index = high

        i = low - 1    # the pointer to smaller nums
        j = high + 1    # the pointer to larger nums

        while True:

            while True:
                i += 1
                if self.arr[i] > self.arr[pivot_index]:
                    break
            while True:
                j -= 1
                if self.arr[j] < self.arr[pivot_index]:
                    break

            if i <= j:
                self.swap(i, j)
        return j




l = [4, 5, 2, 3, 6, 1]
# quick_sort_lomuto = QuickSortLomuto(l)
# quick_sort_lomuto.sort()

quick_sort_hoare = QuickSortHoare(l)
quick_sort_hoare.sort()
print(l)


