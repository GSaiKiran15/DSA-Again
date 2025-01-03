nums = [0,1,2,2,3,0,4,2]
val = 2
output = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[output] = nums[i]
        output += 1
print(output, nums)