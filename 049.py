import eulerlib


def createList(num):
    changeList = []
    for i in range(4):
        a = num[i]
        pre = num[:i]
        if i < 3:
            pre += num[i + 1:]
        for j in range(3):
            b = num[j]
            preNew = pre[:j]
            if j < 2:
                preNew += pre[j + 1:]
            for k in range(2):
                changeList.append(int(a + b + preNew))
                changeList.append(int(a + b + preNew[1] + preNew[0]))
    return changeList


def compute():
    primes = eulerlib.list_primality(10000)
    for i in range(1000, 10000):
        if not primes[i]:
            continue
        changeList = createList(str(i))
        for j in changeList:
            if j <= i:
                continue
            if list.__contains__(changeList, i + (j - i) * 2) and primes[j] and primes[i + (j - i) * 2]:
                print(str(i) + str(j) + str(i + (j - i) * 2))
                break
compute()