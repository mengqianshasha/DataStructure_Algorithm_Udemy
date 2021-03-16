def bubble_sort(arr):
    flag = 1
    while flag:
        flag = 0
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                arr[num], arr[num + 1] = arr[num + 1], arr[num]
                flag = 1

# l = [4, 7, 2, 9, 5, 2, 6, 8, 4, 6, 0, 1, 3, 52, 0, 4, 6]
# bubble_sort(l)
# print(l)

