helo = [2] * 10000001
helo[1] = 0
helo[4] = 1

def compute():
    for i in range(1,len(helo)):
        if helo[i] == 2:
            if getHelo(square(i)):
                helo[i] = 1
            else:
                helo[i] = 0
    ans = sum(1 for i in range(len(helo)) if helo[i] == 1)
    print(ans)


def square(n):
    result = 0
    while n > 0:
        result += SQUARE_DIGITS_SUM[n % 1000]
        n //= 1000
    return result


SQUARE_DIGITS_SUM = [sum(int(c) ** 2 for c in str(i)) for i in range(1000)]


def getHelo(index):
    if helo[index] == 2:
        if getHelo(square(index)):
            helo[index] = 1
            return True
        else:
            helo[index] = 0
            return False
    else:
        if helo[index] == 1:
            return True
        else:
            return False

compute()
