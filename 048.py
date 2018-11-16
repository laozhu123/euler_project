def powers(num):
    sum = 1
    for i in range(num):
        sum *= num
    return sum


def compute():
    sum = 0
    for i in range(1, 1001):
        sum += powers(i)
    print(str(sum)[-10:])

compute()