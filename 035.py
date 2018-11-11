import eulerlib

def compute1():
    primes = eulerlib.list_primality(999999)

    def is_circular_prime(n):
        s = str(n)
        return all(primes[int(s[i:] + s[: i])] for i in range(len(s)))

    ans = sum(1 for i in range(1000000) if is_circular_prime(i))

    return ans


print(compute1())
