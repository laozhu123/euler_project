def getFibonacci():
    pre1,pre2 = 1,1
    for i in range(3,10000):
        if len(str(pre1 + pre2)) == 1000:
            return i
        else:
            pre1,pre2 = pre2,pre1+pre2
print(getFibonacci())
