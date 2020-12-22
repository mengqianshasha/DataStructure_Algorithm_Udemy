from random import choice
from string import ascii_lowercase as letters

list_of_domains = ['yaexample.com','goexample.com','example.com']

list_of_quotes = [  'Luck is what happens when preparation meets opportunity',
            'All cruelty springs from weakness',
            'Begin at once to live, and count each separate day as a separate life',
            'Throw me to the wolves and I will return leading the pack']


def generate_name(length_of_name):
    return ''.join(choice(letters) for _ in range(length_of_name))


def get_domain(domains):
    return choice(domains)


def get_quote(quotes):
    return choice(quotes)


def generate_records(length_of_name, domains, total_records, quotes):
    with open("data.txt", 'w') as to_write:
        for _ in range(total_records):
            key = generate_name(length_of_name) + '@' + get_domain(domains)
            value = get_quote(quotes)
            to_write.write(key + ':' + value + '\n')
        to_write.write("mashrur@example.com:Don't let me leave Murph\n")
        to_write.write("evgeny@example.com:All I do is win win win no matter what!\n")


generate_records(10, list_of_domains, 10, list_of_quotes)
