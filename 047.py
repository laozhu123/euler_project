import eulerlib


def isFourPrimes(num, primes):
    diff = 0
    i = 0
    change = True
    while True:
        if num % primes[i] == 0:
            if change:
                diff += 1
                change = False
            num /= primes[i]
        else:
            change = True
            i += 1
        if diff == 4 and num == 1:
            return True
        if num == 1:
            return False


def compute():
    primes = eulerlib.list_primes(1000000)
    num = 0
    for i in range(4, 1000000):
        if isFourPrimes(i, primes):
            num += 1
        else:
            num = 0
        if num == 4:
            print(i - 3)
            break


compute()
