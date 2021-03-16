def decimal_to_binary(num):
    # Unintentional case: negative number, float

    # Base case
    if num == 0:
        return 0

    # Recursion
    quotient = num // 2
    remainder = num % 2
    return 10 * decimal_to_binary(quotient) + remainder


print(decimal_to_binary(5))
