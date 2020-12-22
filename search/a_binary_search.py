# iteration solution
def binary_search1(n, arr):
    start = 0
    stop = len(arr)-1

    while start < stop:
        mid = (start+stop)//2
        if n == arr[mid]:
            return f'{n} found at index: {mid}'
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1

    return f'{n} not found in list'

# recursion solution
def binary_search2(n, arr, start, stop):
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


l = [2,5,7,9,34,78,145,345]
# print(binary_search(8,l))
print(binary_search2(3, l, 0, len(l)-1))



