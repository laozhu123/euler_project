def compute():
    for i in range(285, 1000000):
        num1 = int(i * (i + 1) / 2)
        ok = True
        for j in range(int(pow(num1 * 2 / 3, 1 / 2)), 10000000):
            num2 = int(j * (3 * j - 1) / 2)
            if num2 > num1:
                ok = False
                break
            if num1 == num2:
                break
        if not ok:
            continue
        for j in range(int(pow(num1 / 2, 1 / 2)), 10000000):
            num2 = j * (2 * j - 1)
            if num2 > num1:
                ok = False
                break
            if num1 == num2:
                break
        if ok:
            print(num1)
compute()
