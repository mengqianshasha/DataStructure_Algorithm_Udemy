from a_bubble_sort import *
from b_selection_sort import *
from c_insertion_sort import *
from d_merge_sort import *
from e_quick_sort import *
import time
from random import randint

# decide the size of the list
while True:
    size = int(input("What size list do you want to create? "))
    if size > 0:
        break

# decide the max value of the range
while True:
    max_num = int(input("What is the max value of the range? "))
    if max_num > 0:
        break

# decide the times of execution of the program
while True:
    cycles = int(input("How many times do you want to run? "))
    if cycles > 0:
        break


def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    elapse = toc - tic
    print(f'{func_name.__name__: <18}-> Elapsed time: {elapse:1.5f}')


for cycle in range(cycles):
    print(f'Run: {cycle+1}')
    l = [randint(0, max_num) for _ in range(size)]

    # analyze_func(bubble_sort, l.copy())
    # analyze_func(selection_sort, l.copy())
    # analyze_func(insertion_sort, l.copy())
    analyze_func(merge_sort, l)
    analyze_func(quick_sort, l)
    analyze_func(sorted, l)
    print('-'*40)


# l = [2,1]
# selection_sort2(l)
# print(l)



