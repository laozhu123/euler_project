def isPrime(num):
    for i in range(2, int(abs(num) / 2)):
        if num % i == 0:
            return False
    return True


def findMax(x, y):
    for i in range(1000):
        if isPrime(i * i + x * i + y):
            continue
        else:
            return i


max = 0
num1, num2 = 0, 0
for i in range(-999, 1000):
    for j in range(-999, 1000):
        helo = findMax(i, j)
        print(helo, i, j)
        if max < helo:
            max, num1, num2 = helo, i, j
print(num1 * num2)
