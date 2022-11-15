def get_perfect_numbers(n):
    res = []
    i = 1
    while n > 0:
        dividers = []
        for j in range(1, i):
            if i % j == 0:
                dividers.append(j)
        if sum(dividers) == i:
            res.append(i)
            n -= 1
        i += 1

    return res


print(get_perfect_numbers(3))
