import eulerlib

def compute():
    primes = eulerlib.list_primality(7071)
    helo = [False]*(5*10**7)
    for i in range(7071):
        if primes[i]:
            for j in range(368):
                if i ** 2 + j ** 3 > len(helo) - 1:
                    break
                if primes[j]:
                    for k in range(84):
                        if i**2+j**3+k**4 > len(helo)-1:
                            break
                        if primes[k]:
                            helo[i**2+j**3+k**4] = True
    ans = 0
    for i in range(len(helo)):
        if helo[i]:
            ans += 1
    return ans

print(compute())