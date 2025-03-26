nums = [3,2,2,3]
val = 3
output = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[output] = nums[i] 
        output += 1
print(output)