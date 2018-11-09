def diffcult():
    val = 1
    for i in range(10):
        if i == 0:
            continue
        val = val * (i+10)
        print(i)
        print(val)
        while True:
            if val % 10 == 0:
                val /= 10
            else:
                break
        val %= 100000
    print(val)

def helo():
    val = 1
    num = 2496
    for i in range(9):
        val = val * num
        while True:
            if val % 10 == 0:
                val /= 10
            else:
                break
        val %= 100000
    print(val*36288)


if __name__ == '__main__':
    diffcult()
    # helo()