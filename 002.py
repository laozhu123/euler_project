# def diffcult():
#     list = [1,2]
#     getFibonacci(list)
#     sum = 0
#     for i in range(len(list)):
#         print(list[i])
#         if list[i] % 2 == 0:
#             sum += list[i]
#     print(sum)
#
# def getFibonacci(list):
#
#     while True:
#         if list[len(list)-1]+list[len(list)-2] < 4000000:
#             list.append(list[len(list)-1]+list[len(list)-2])
#         else:
#             break
#     return
#
# if __name__ == '__main__':
#     diffcult()


def compute():
    ans = 0
    x = 1  # Represents the current Fibonacci number being processed
    y = 2  # Represents the next Fibonacci number in the sequence
    while x <= 4000000:
        if x % 2 == 0:
            ans += x
        x, y = y, x + y
    return str(ans)


if __name__ == "__main__":
    print(compute())
