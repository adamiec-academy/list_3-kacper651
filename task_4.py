def tower(n):
    for i in range(n):
        print((n - (i + 1)) * " " + (i + 1) * "#" + i * "#")
        print((n - (i + 1)) * " " + (i + 1) * "#" + i * "#")
        print((n - (i + 1)) * " " + (i + 1) * "#" + i * "#")


def towers(data):
    pass


tower(4)
towers([2, 1, 3])
