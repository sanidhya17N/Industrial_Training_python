import functools


def MUL(a, b):
    return a*b


L = [10, 20, 30, 40, -1, 50, -2, -5]
result = functools.reduce(MUL, L)
print(result)
