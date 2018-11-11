money = [1, 2, 5, 10, 20, 50, 100, 200]


def coinSums(leave, index):
    sum = 0
    if index == 0 or leave == 0:
        return 1
    else:
        if leave >= money[index]:
            sum += coinSums(leave - money[index], index)
        sum += coinSums(leave, index - 1)
    return sum


print(coinSums(200, 7))
