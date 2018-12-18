
def compute(n):
    result = list(range(n + 1))
    print(result)
    for i in range(2, len(result)):
        if result[i] == i:
            for j in range(i, len(result), i):
                result[j] -= result[j]//i
    print(result)
    return sum(result)


if __name__ == "__main__":
    print(compute(9))


# import eulerlib, itertools
#
#
# def compute():
# 	totients = eulerlib.list_totients(9)
# 	ans = sum(itertools.islice(totients, 2, None))
# 	return str(ans)
#
#
# if __name__ == "__main__":
# 	print(compute())