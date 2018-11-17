def getCombinatoric(num, index):
    sum = 1
    for i in range(index):
        sum *= (num - i)
        sum /= (i + 1)
    return sum


def compute():
    num = 0
    for i in range(3, 101):
        for j in range(2, i):
            if getCombinatoric(i, j) >= 1000000:
                num += i - j - j + 1
                break
    print(num)

compute()