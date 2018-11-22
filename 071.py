def compute():
    max = 0
    a, b = 0, 0
    for i in range(100, 1000001):
        t = int((i * 3) / 7)
        if t / i == 3 / 7:
            if float(t - 1) / i > max:
                max = float(t - 1) / i
                print(max)
                a = t - 1
                b = i
        else:
            if t / i > max:
                max = float(t) / i
                print(max)
                a = t
                b = i
    print(a, b)


compute()
