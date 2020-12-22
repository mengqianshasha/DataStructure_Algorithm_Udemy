def insertion_sort(my_list):
    for outer_index in range(1, len(my_list)):
        index = outer_index
        while index:
            if my_list[index] < my_list[index - 1]:
                my_list[index - 1], my_list[index] = my_list[index], my_list[index - 1]
                index -= 1
            else:
                break


# l = [8, 4, 6, 2, 6, 3, 5, 90, 4, 6]
# insertion_sort(l)
# print(l)
