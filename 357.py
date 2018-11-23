# 查看规律，是求e的渐进分数
# 2    1
# 3    2
# 8    1
# 11   1
# 19   4
# 87   1
# 106  1
# 193  6
# 299  1
# 看出规律了吗

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