def diffcult():
    list = [1,2]
    getFibonacci(list)
    sum = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            sum += list[i]
    print(sum)

def getFibonacci(list):

    while True:
        if list[len(list)-1]+list[len(list)-2] < 4000000:
            list.append(list[len(list)-1]+list[len(list)-2])
        else:
            break
    return

if __name__ == '__main__':
    diffcult()
