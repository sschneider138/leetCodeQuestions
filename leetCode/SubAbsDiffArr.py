nums = [2, 3, 5]
newNums = []


def slow():
    for i in range(0, len(nums)):
        tmp = nums[i]
        count = 0
        for num in nums:
            count += abs(tmp - num)
        newNums.append(count)
    return newNums


print(fast())
