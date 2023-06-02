def calFactorial(a):
    if a == 1 or a == 0:
        return a
    return a*calFactorial(a-1)


x = int(input("Enter a Number\n"))
print(calFactorial(x))
