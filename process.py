def proc():
    fr = open('/Users/daisycc/lagou/qiubai.txt', 'r')

    fw = open('/Users/daisycc/lagou/pro.txt', 'w')
    for i in range(6000):
        hh = fr.readline()
        if hh.__contains__('点赞'):
            cs = hh.split(" ")
            for j in range(len(cs)):
                if cs[j].__contains__('点赞'):
                    cts = cs[j].split("：")
                    if len(cts) >= 2:
                        if int(cts[1]) > 2000:
                            for t in range(6):
                                fw.write(fr.readline())
    fr.close()
    fw.close()


def proc2():
    fr = open('/Users/daisycc/lagou/qiubai.txt', 'r')
    fw = open('/Users/daisycc/lagou/pro2.txt', 'w')
    t = 1
    f = 1  # empty
    for i in range(6000):
        sl = fr.readline()
        if len(sl) > 10:
            if f != 0:
                fw.write(str(t) + ".")
                t += 1
                f = 0
            fw.write(sl)
        else:
            f = 1
    fr.close()
    fw.close()


if __name__ == '__main__':
    # proc()
    proc2()
