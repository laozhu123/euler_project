def compute():
    sum = 1
    helo = 8589934592
    for i in range(7830457 // 33):
        sum = (sum * helo) % 10000000000

    for i in range(7830457 % 33):
        sum = (sum * 2) % 10000000000

    sum = (sum * 28433 + 1) % 10000000000
    print(sum)

compute()
