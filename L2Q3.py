def Calculator(in1, in2=0):
    a = in1+in2
    s = in1-in2
    m = in1*in2
    if in2 == 0:
        d = 0
    else:
        d = in1/in2
    return (a, s, m, d)


print(Calculator(2, 5))
