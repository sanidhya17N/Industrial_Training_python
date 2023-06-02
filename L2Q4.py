def proc(x):
    x = 2*x*x
    return x


def main():
    num = 10

    #  proc(num) This function returned 200 but num wasn't assigned the returned value , hence print gave 10
    # just change num=proc(num)
    num = proc(num)
    print(num)


main()
