import eulerlib


def compute():
    primes = eulerlib.list_primality(999999)

    def is_truncatable(num):
        return all(primes[int(str(num)[:i])] for i in range(1, len(str(num)))) and all(
            primes[int(str(num)[i:])] for i in range(len(str(num))))

    return sum(i for i in range(10, 999999)if is_truncatable(i))

print(compute())
