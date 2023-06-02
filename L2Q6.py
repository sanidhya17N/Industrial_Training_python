def print_big_enough(L, x):
    L = list(filter(lambda a: a >= x, L))
    print(L)


L = [10, 20, -1, -10, -20, 30, 40]
print_big_enough(L, -5)
