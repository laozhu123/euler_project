
# 大傻逼题目都看错了

# import eulerlib
#
# primes = eulerlib.list_primality(19999999)
#
#
# def getList(num, pre, list):
#     if num == 1:
#         list.append(pre + "0")
#         list.append(pre + "1")
#     else:
#         getList(num - 1, pre + "0", list)
#         getList(num - 1, pre + "1", list)
#
#
# def compute():
#     for i in range(10000019, 10000020, 2):
#         if primes[i]:
#             if str(i).__contains__('0'):
#                 num = 0
#                 for j in range(8):
#                     if str(i)[j] == "0":
#                         num += 1
#                 list = []
#                 getList(num, "", list)
#                 realOk = False
#                 for l in list:
#                     haveOne = False
#                     for s in range(len(l)):
#                         if l[s] == "1":
#                             haveOne = True
#                             break
#                     if not haveOne:
#                         continue
#                     list2 = [str(i)] * 9
#                     for k in range(len(l)):
#                         if l[k] == "1":
#                             index = 0
#                             zeroNum = 0
#                             for f in range(len(str(i))):
#                                 if str(i)[f] == "0":
#                                     zeroNum += 1
#                                 if zeroNum == k + 1:
#                                     index = f
#                                     break
#                             for s in range(len(list2)):
#                                 list2[s] = list2[s][:index] + str(s + 1) + list2[s][index + 1:]
#                     isOk = True
#                     for l in list2:
#                         if not primes[int(l)]:
#                             print(l, "is not prime")
#                             isOk = False
#                             break
#                     if isOk:
#                         print(list2)
#                         realOk = True
#                         break
#                 if realOk:
#                     break
#
#
# compute()


import eulerlib


def compute():
    isprime = eulerlib.list_primality(1000000)
    for i in range(len(isprime)):
        if not isprime[i]:
            continue

        n = [int(c) for c in str(i)]
        for mask in range(1 << len(n)):
            digits = do_mask(n, mask)
            count = 0
            for j in range(10):
                if digits[0] != 0 and isprime[to_number(digits)]:
                    count += 1
                    print(to_number(digits))
                digits = add_mask(digits, mask)

            if count == 8:
                digits = do_mask(n, mask)
                for j in range(10):
                    if digits[0] != 0 and isprime[to_number(digits)]:
                        return str(to_number(digits))
                    digits = add_mask(digits, mask)
    raise AssertionError("Not found")


def do_mask(digits, mask):
    return [d * ((~mask >> i) & 1) for (i, d) in enumerate(digits)]


def add_mask(digits, mask):
    return [d + ((mask >> i) & 1) for (i, d) in enumerate(digits)]


def to_number(digits):
    result = 0
    for d in digits:
        result = result * 10 + d
    return result


if __name__ == "__main__":
    print(compute())