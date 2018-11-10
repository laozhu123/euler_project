sum = 1
pre = 4
for i in range(1,501):
    sum += pre+i*2*10
    pre += i*2*4*4
print(sum)