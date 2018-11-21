def compute():
    sum = 0
    for i in range(1,10):
        for j in range(1,100):
            if len(str(pow(i,j))) < j:
                break
            else:
                print(i,j)
                sum += 1
    print(sum)

compute()