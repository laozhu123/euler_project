import eulerlib


def compute():
    primes = eulerlib.list_primes(1000000)
    isPrimes = eulerlib.list_primality(1000000)
    max = 0
    maxConsecutive = 0
    for i in range(len(primes)):
        sum = 0
        length = 0
        for j in range(i, len(primes)):
            sum += primes[j]
            length += 1
            if sum > 1000000:
                break
            if isPrimes[sum]:
                if length > maxConsecutive:
                    max = sum
                    maxConsecutive = length
    print(max)
compute()