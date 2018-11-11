sum = 0
for i in range(2,1000000):
    preSum = 0
    for t in str(i):
        preSum += int(t)**5
    if preSum == i:
        sum += i
print(sum)