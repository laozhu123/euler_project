def compute():
    factorial = []
    factorial.append([0]*101)
    for i in range(1,101):
        factorial.append([0] * 101)
        for j in range(1,101):
            if i == 1 or j == 1:
                factorial[i][j] = 1
            elif j > i:
                factorial[i][j] = factorial[i][i]
            elif i == j:
                factorial[i][j] = factorial[i][j-1]+1
            elif i > j:
                factorial[i][j] = factorial[i-j][j] + factorial[i][j-1]
    print(factorial[100][99])

compute()