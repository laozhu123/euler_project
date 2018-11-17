def compute():
    sum = 0
    for i in range(10000):
        isLychrel = True
        n = i
        for j in range(50):
            n += int(str(n)[:: -1])
            if n == int(str(n)[:: -1]):
                isLychrel = False
                break
        if isLychrel:
            sum += 1
    print(sum)

compute()