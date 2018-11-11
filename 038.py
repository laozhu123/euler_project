def max_pandigital():
    max = 0
    for i in range(1, 9328):
        preS = ""
        for j in range(1, 10):
            preS += str(j * i)
            if len(preS) == 9:
                l = list(preS)
                l.sort()
                if "".join(l) == "123456789" and max < int(preS):
                    max = int(preS)
    return max


print(max_pandigital())
