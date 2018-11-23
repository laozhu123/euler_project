def compute():
    rect = []
    for i in range(12001):
        rect.append([0] * 12001)
    sum = 0
    for i in range(5, 12001):
        for j in range(i // 3, i // 2 + 1):
            if j / i > 1 / 3 and j / i < 1 / 2:
                if rect[i][j] == 0:
                    sum += 1
                    if i <= 12000 / 2:
                        for k in range(2, int(12000 / i) + 1):
                            rect[i*k][j*k] = 1

    print(sum)


compute()
