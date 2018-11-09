def diffcult():
    print(getLargestFactor(600851475143))


def getLargestFactor(num):
    if num <= 2:
        return 2
    for i in range(num):
        if num % (i + 2) == 0:
            if i + 2 > getLargestFactor(int(num / (i + 2))):
                return i + 2
            else:
                return getLargestFactor(int(num / (i + 2)))
    return num


if __name__ == '__main__':
    diffcult()
