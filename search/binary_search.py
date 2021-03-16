# Solution 1: iteration
# Time: O(logN)
def binary_search_1(n, arr):
    start = 0
    stop = len(arr)-1

    while start <= stop:
        mid = (start+stop)//2
        if n == arr[mid]:
            return f'{n} found at index: {mid}'
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1

    return f'{n} not found in list'


# Solution 2: Recursion
# Time: O(logN)
def binary_search_2(n, arr, start, stop):
    if start > stop:
        return f'{n} not found in list'
    else:
        mid = (start+stop)//2
        if n == arr[mid]:
            return f'{n} found at index: {mid}'
        elif n < arr[mid]:
            stop = mid - 1
            return binary_search2(n, arr, start, stop)
        else:
            start = mid + 1
            return binary_search2(n, arr, start, stop)

####
l = [1,2,3,4]
print(binary_search_3(5, l))



