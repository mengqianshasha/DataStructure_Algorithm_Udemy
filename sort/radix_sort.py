from collections import deque


class RadixSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        # find out the len of the largest number
        num_digits = len(str(max(self.arr)))

        # loop len times to counting sort, once a digit
        for i in range(num_digits):
            self.counting_sort(i)

    def counting_sort(self, digit):
        # Empty counting arr with 10 empty buckets at first
        counting_arr = [deque() for _ in range(10)]

        # Put a num to a bucket according to its value on a specific digit
        for num in self.arr:
            index = (num // (10 ** digit)) % 10
            counting_arr[index].append(num)

        # Copy all numbers back to original arr in order
        k = 0
        for bucket in counting_arr:
            while bucket:
                self.arr[k] = bucket.popleft()  # deque pop: O(1), list pop: O(N)
                k += 1


if __name__ == '__main__':
    arr = [71, 85, 36, 66, 47, 40, 6, 99]
    radix_sort = RadixSort(arr)
    radix_sort.sort()
    print(arr)


