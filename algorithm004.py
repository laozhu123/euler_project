def diffcult():
    print(getLargestPalindrome(1000))


def getLargestPalindrome(num):
    for i in range(num):
        if i == 0:
            continue
        first = str(num - i)
        first += first[2] + first[1] + first[0]
        helo = int(first)
        for i in range(1000):
            if i == 0:
                continue
            if helo % (1000 - i) == 0:
                if helo/(1000-i) >= 100:
                    if helo/(1000-i) < 1000:
                        return helo

if __name__ == '__main__':
    diffcult()
