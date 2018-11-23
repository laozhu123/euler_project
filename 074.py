motor = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}


def get_factorial(num):
    return int(sum(motor[num[i]] for i in range(len(num)) if True))


def compute():
    sum = 0
    for i in range(1, 10**6):
        helo = [str(i)]
        sum += 1
        for j in range(59):
            t = get_factorial(str(helo[-1]))
            if helo.__contains__(str(t)):
                sum -= 1
                break
            else:
                helo.append(str(t))
    print(sum)

compute()
