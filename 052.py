def compute():
    for i in range(1, 100000000):
        isOk = True
        for be in range(2, 7):
            if sorted(str(i * be)) != sorted(str(i)):
                isOk = False
                break
        if isOk:
            print(i)
            break


compute()
