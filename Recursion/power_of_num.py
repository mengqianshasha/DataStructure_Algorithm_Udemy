def power_of_num(base, expo):
    assert expo >= 0 and int(expo) == expo, "The exponent should be a positive int"

    if expo == 0:
        return 1
    return base * power_of_num(base, expo - 1)


print(power_of_num(2, 7))