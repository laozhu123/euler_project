import numpy

def isFactorials(num):
    preSum = sum(numpy.math.factorial(int(s)) for s in str(num))
    if num == preSum:
        return True
    return False

print(sum(i for i in range(10, 1000000) if isFactorials(i)))
