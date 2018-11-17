import eulerlib


def compute():
    primeNum = 0
    num = 1
    all = 1
    for i in range(1, 30000):
        for j in range(1, 5):
            # print(num + 2 * i * j)
            if eulerlib.is_prime(num + 2 * i * j):
                primeNum += 1
                # print(num + 2 * i * j)
        num += 2 * i * j
        all += 4
        print(primeNum / all)
        if primeNum / all < 0.1:
            print(i * 2 + 1)
            break


compute()
