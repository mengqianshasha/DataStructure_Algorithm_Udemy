from random import choice
from string import ascii_lowercase
import time


def binary_search(n, arr):
    start = 0
    stop = len(arr)-1

    while start <= stop:
        mid = (start+stop)//2
        if n == arr[mid]:
            return mid, f'{n} found at index: {mid}'
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1

    return None, f'{n} not found in list'


def analyze_func(func_name, *args):
    tic = time.time()
    func_name(*args)
    toc = time.time()
    elapse = toc - tic
    print(f'{func_name.__name__: <18}-> Elapsed time: {elapse:1.5f}')


def generate_name(length_of_name):
    return ''.join([choice(ascii_lowercase) for i in range(length_of_name)])


def get_domain(list_of_domains):
    return choice(list_of_domains)


def generate_emails(length_of_name, list_of_domains, total_emails):
    email_list = []
    for i in range(total_emails):
        email_list.append(generate_name(length_of_name)+'@'+get_domain(list_of_domains))
    return email_list