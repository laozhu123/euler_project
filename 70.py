def sort(num):
    return sorted(str(num))


def compute(n):
    result = list(range(n + 1))
    for i in range(2, len(result)):
        if result[i] == i:
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
    min = 100.0
    n = 0
    for i in range(3, len(result)):
        if sort(i) == sort(result[i]):
            if float(i) / result[i] < min:
                min = float(i) / result[i]
                n = i
    return n, min


if __name__ == "__main__":
    print(compute(10 ** 7))
