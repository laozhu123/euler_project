def compute():
    t1 = 2
    t2 = 0
    for i in range(1, 100):
        if i == 1:
            t2 = 3
        else:
            if i % 3 == 2:
                t = t2
                t2 = (int(i/3)+1)*2*t2+t1
                t1 = t
            else:
                t = t2
                t2 = t2+t1
                t1 = t
    ans = sum(int(str(t2)[i]) for i in range(len(str(t2))) if True)
    print(ans)

compute()