import eulerlib


def compute():
    primes = eulerlib.list_primality(999999)

    def is_circular_prime(n):
        s = str(n)
        return all(primes[int(s[i:] + s[: i])] for i in range(len(s)))

    return sum(1 for i in range(1000000) if is_circular_prime(i))


print(compute())
