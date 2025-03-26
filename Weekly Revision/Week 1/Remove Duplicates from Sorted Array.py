nums = [0,0,1,1,1,1,2,3,3]
index = 1
for i in range(2, len(nums)):
    if nums[i-1] == nums[i] and nums[i-2] == nums[i]:
        nums[index] = nums[i]
        index += 1
print(nums)
