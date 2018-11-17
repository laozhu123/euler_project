def compute():
    sum = 0
    x = 1
    y = 2
    for i in range(1000):
        z = y + x
        if len(str(z)) > len(str(y)):
            sum += 1
        prey = y * 2 + x
        x = y
        y = prey
    print(sum)

compute()
