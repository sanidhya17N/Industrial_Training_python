def FINDMAX(a, b):
    return a if a > b else b


a = int(input("enter 1st Number\n"))
b = int(input("enter 2nd Number\n"))
x = FINDMAX(a, b)
print(x)

L = [10, 20, 30, 40, -1, 50, -2, -5]
while len(L) > 1:
    L = list(map(FINDMAX, L[::2], L[1::2]))
print(L[0])
