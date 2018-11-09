def createAbundantList():
    LIMIT = 28124
    divisorsum = [0] * LIMIT
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisorsum[j] += i
    abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]
    return abundantnums


def createFinalList(list):
    finalList = [False] * 28124
    for i in list:
        for j in list:
            if i + j <= 28123:
                finalList[i + j] = True
            else:
                break
    return finalList


def main():
    list = createAbundantList()
    finalList = createFinalList(list)
    ans = sum(i for (i, value) in enumerate(finalList) if not value)
    print(ans)


main()
