import eulerlib


def compute():
    DIGITS = 100
    MULTIPLIER = 100 ** DIGITS
    ans = sum(
        sum(int(c) for c in str(eulerlib.sqrt(i * MULTIPLIER))[: DIGITS])
        for i in range(100)
        if eulerlib.sqrt(i) ** 2 != i)
    return str(ans)


if __name__ == "__main__":
    print(compute())
