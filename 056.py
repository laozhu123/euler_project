def compute():
    max = 0
    for a in range(100):
        for b in range(100):
            x = pow(a, b)
            sum = 0
            for index in range(len(str(int(x)))):
                sum += int(str(x)[index])
            if sum > max:
                max = sum
    print(max)


compute()
