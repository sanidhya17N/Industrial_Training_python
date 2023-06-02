def multiply():
    L = [10, 20, 30, 40, -1, 50, -2, -5]
    L1 = [x*2 for x in L]
    print(L1)

    L2 = [x*2 for x in L if x > 0]
    print(L2)


multiply()
