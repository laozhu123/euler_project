def compute():
    nums = [0] * 3001
    for i in range(1, 3001):
        nums[i] = int((3 * i * i - i) / 2)
    min = 10000

    for j in range(1, 3001):
        print(i)
        for i in range(1, j):
            if nums.__contains__(nums[j] - nums[i]) and nums.__contains__(nums[j] + nums[i]):
                return nums[j] - nums[i]
print(compute())
