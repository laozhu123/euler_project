import eulerlib


def compute():
    totients = eulerlib.list_totients(10 ** 6)
    max = 0
    t = 2
    for i in range(2,len(totients)):
        if i/totients[i] > max:
            max = i/totients[i]
            t = i
    return t


if __name__ == "__main__":
    print(compute())
