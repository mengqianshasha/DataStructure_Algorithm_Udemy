def selection_sort1(l):
    for index in range(len(l)-1):
        for num in range(index+1, len(l)):
            if l[index] > l[num]:
                l[index], l[num] = l[num], l[index]


def selection_sort(l):
    spot_marker = 0
    while spot_marker < len(l)-1:
        for num in range(spot_marker+1, len(l)):
            if l[spot_marker] > l[num]:
                l[spot_marker], l[num] = l[num], l[spot_marker]
        spot_marker += 1


# l1 = [7,4,6,3,5,4,6,5,4,3,6]
# l2 = [7,4,6,3,5,4,6,5,4,3,6]
# selection_sort1(l1)
# selection_sort(l2)
# print(l1)
# print(l2)