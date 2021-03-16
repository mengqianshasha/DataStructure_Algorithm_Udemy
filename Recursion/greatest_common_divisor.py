# Euclidean algorithm
def gcd(n1, n2):
    assert int(n1) == n1 and int(n2) == n2, "The two nums should be int"

    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)


print(gcd(18, 48))
