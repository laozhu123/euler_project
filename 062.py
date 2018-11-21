def compute():
    dict1 = {}
    for i in range(100000):
        sum = pow(i, 3)
        s = "".join(sorted(str(sum)[0:]))
        if not dict1.__contains__(s):
            dict1[s] = "1_" + str(sum)
        else:
            ss = dict1[s].split("_")
            if ss[0] == "4":
                print(ss[1])
                return
            dict1[s] = str(int(ss[0]) + 1) + "_" + ss[1]


compute()
