def compute():
    return sum(i for i in range(1, 10000) if isPandigital(i))

def isPandigital(num):
    for i in range(1, int(pow(num, 1 / 2)) + 1):
        if num % i == 0:
            if "".join(sorted(str(num) + str(num // i) + str(i))) == "123456789":
                return True
    return False


print(compute())
