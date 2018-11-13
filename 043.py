num = "0123456789"
divs = [2, 3, 5, 7, 11, 13, 17]


def is_divisibility(nstr):
    return all(int(nstr[i + 1:i + 4]) % divs[i] == 0 for i in range(len(divs)) if True)


def get_divisibility(strs, index, prefix):
    sum = 0

    if index == 9:
        if is_divisibility(prefix + strs):
            return int(prefix + strs)
        else:
            return 0
    num = 9 if index == 0 else len(strs)
    for i in range(num):
        pre = strs
        sum += get_divisibility(pre.replace(strs[i], ''), index + 1, prefix + strs[i])
    return sum


def compute():
    print(get_divisibility(num, 0, ""))


compute()
