def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return[]

print(twoSum([2,7,11,15], 9))



