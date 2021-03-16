# Right to left
# def sum_of_digits(n):
#     assert n >= 0 and int(n) == n, "The input must be a positive integer."
#     if len(str(n)) == 1:
#         return n
#     else:
#         num_of_digits = len(str(n))
#         return n // (10 ** (num_of_digits - 1)) + sum_of_digits(n % (10 ** (num_of_digits - 1)))

# Left to right: better
def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "The input must be a positive integer."
    if n == 0:
        return 0
    else:
        return sum_of_digits(n // 10) + (n % 10)


print(sum_of_digits(436))
