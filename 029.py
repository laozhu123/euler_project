# helo = [[False] * 102 for row in range(102)]
#
# sum = 0
# for i in range(2, 15):
#     for j in range(2, 15):
#         if not helo[i][j]:
#             sum += 1
#             for x in range(2, j):
#                 if j % x == 0 and j / x >= 2:
#                     t = i
#                     for y in range(x - 1):
#                         t *= i
#                     if t <= 8:
#                         helo[t][int(j / x)] = True
#                 elif j / x < 2:
#                     break
#             for x in range(2, int(j / 2)):
#                 sqrt = pow(i, 1.0 / x)
#                 if sqrt >= 2 and sqrt % 1 == 0:
#                     for k in range(2, x * j):
#                         t = int(sqrt)
#                         h, q = divmod(x * j, k)
#                         if q == 0:
#                             for s in range(k - 1):
#                                 t *= int(sqrt)
#                             if t > 14:
#                                 break
#                             if x * j / k > 14:
#                                 continue
#                             else:
#                                 print(t, h)
#                                 helo[t][h] = True
#                 if sqrt < 2:
#                     break
# print(sum)


# 速度有影响，但是我上面的代码好像有问题
# We generate all the possible powers in the given range, put each value
# into a set, and let the set count the number of unique values present.
def compute():
	seen = set(a**b for a in range(2, 101) for b in range(2, 101))
	return str(len(seen))


if __name__ == "__main__":
	print(compute())