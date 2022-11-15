def fibonacci_sequence(n):
    n0 = 0
    n1 = 1
    res = []

    while n > 0:
        res.append(n0)
        n2 = n0 + n1
        n0 = n1
        n1 = n2
        n -= 1

    return res


print(fibonacci_sequence(9))
