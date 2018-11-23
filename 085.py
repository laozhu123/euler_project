def get_counting(x, y):
    sum = 0
    for i in range(x):
        for j in range(y):
            sum += (x - i) * (y - j)
    return sum


def compute():
    m = 2000000
    x,y = 0,0
    for i in range(1, 100):
        for j in range(1, 100):
            t = get_counting(i, j)
            if abs(2000000 - t) < m:
                m = abs(2000000 - t)
                x = i
                y = j
            if t > 2000000:
                break
    print(m,x,y,x*y)


compute()
