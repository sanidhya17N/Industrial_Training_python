def Addlist(L1, L2):
    L3 = list(map(lambda x, y: x+y, L1, L2))
    return L3


L1 = [1, 2, 3, 4]
L2 = [10, 20, 30, 40]
print(Addlist(L1, L2))
