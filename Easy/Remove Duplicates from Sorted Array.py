nums = [1,1,2]
index = 1
for i in range(1,len(nums)):
    if nums[i-1] != nums[i]:
        nums[index] = nums[i]
        index += 1
print(index)             