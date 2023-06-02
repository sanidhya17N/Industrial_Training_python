def isPositive(a):
    return True if a > 0 else False


x = int(input("Enter a Number\n"))
print(isPositive(x))

L = [10, 20, 30, 40, -1, 50, -2, -5]
L = list(filter(isPositive, L))
print(L)
