import eulerlib


def compute():
    primes = eulerlib.list_primality(1000000)
    for i in range(33, 1000000, 2):
        if primes[i]:
            continue
        isOk = True
        for j in range(1, int(pow(i / 2, 1 / 2)) + 1):
            if primes[i - j * j * 2]:
                isOk = False
                break
        if isOk:
            print(i)
            break


compute()


# import eulerlib, itertools, sys
#
# if sys.version_info.major == 2:
#     filterfalse = itertools.ifilterfalse
# else:
#     filterfalse = itertools.filterfalse
#
#
# def compute():
#     # ans = next(filterfalse(test_goldbach, itertools.count(9, 2)))
#     print(test_goldbach(57))
#     # return str(ans)
#
#
# def test_goldbach(n):
#     if n % 2 == 0 or eulerlib.is_prime(n):
#         return True
#     for i in itertools.count(1):
#         k = n - 2 * i * i
#         if k <= 0:
#             return False
#         elif eulerlib.is_prime(k):
#             print(k)
#             return True
#
#
# if __name__ == "__main__":
#     print(compute())
