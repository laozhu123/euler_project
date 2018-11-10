def getCycle(num):
    values = [0]*1000
    values[1] = 1
    values[10] = 2
    values[100] = 3
    mother = 1
    i = 1
    while True:
        if num > mother:
            mother *= 10
        else:
            r, q = divmod(mother, num)
            if q == 0:
                return 0
            else:
                if values[q] != 0:
                    return i - values[q]
                else:
                    values[q] = i
        i += 1

def helo():
    max1 = 0
    index = 0
    for i in range(1,1000):
        len = getCycle(i)
        if  len > max1:
            max1 = len
            index = i
    return index

print(helo())