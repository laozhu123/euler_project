import numpy


def is_factorials(num):
    pre_sum = sum(numpy.math.factorial(int(s)) for s in str(num))
    if num == pre_sum:
        return True
    return False


print(sum(i for i in range(10, 1000000) if is_factorials(i)))
