def compute():
    for i in range(1000, 10000):
        if i % 100 < 10:
            continue
        t = int(pow(i * 2, 0.5))
        if t * (t + 1) != i * 2:
            continue
        h = [i]
        square(i % 100, i / 100, i, h)


def square(end, head, s, h):
    for i in range(end * 100, (end + 1) * 100):
        if i % 100 < 10:
            continue
        t = int(pow(i, 0.5))
        if t * t != i:
            continue
        h.append(i)
        pentagonal(i % 100, head, s + i, h)


def pentagonal(end, head, s, h):
    for i in range(end * 100, (end + 1) * 100):
        if i % 100 < 10:
            continue
        t = int(pow(i * 2 / 3, 0.5)) + 1
        if t * (3 * t - 1) != i * 2:
            continue
        h.append(i)
        hexagonal(i % 100, head, s + i, h)


def hexagonal(end, head, s, h):
    for i in range(end * 100, (end + 1) * 100):
        if i % 100 < 10:
            continue
        t = int(pow(i / 2, 0.5)) + 1
        if t * (2 * t - 1) != i:
            continue
        h.append(i)
        sum = heptagonal(i % 100, head, s + i, h)


def heptagonal(end, head, s, h):
    for i in range(end * 100, (end + 1) * 100):
        if i % 100 < 10:
            continue
        t = int(pow(i * 2 / 5, 0.5)) + 1
        if t * (5 * t - 3) / 2 != i:
            continue
        h.append(i)
        sum = octagonal(i % 100, head, s + i, h)


def octagonal(end, head, s, h):
    for i in range(end * 100, (end + 1) * 100):
        if i % 100 < 10:
            continue
        t = int(pow(i / 3, 0.5)) + 1
        if t * (3 * t - 2) != i:
            continue
        print(h, i)
        if i % 100 == head:
            print(s + i)
            return

# compute()
def test():
    for i in range(1, 100):
        t = int(pow(i / 3, 0.5)) + 1
        if t * (3 * t - 2) != i:
            continue
        print(i)

test()