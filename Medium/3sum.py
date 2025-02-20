nums = [-1,0,1,2,-1,-4]
output = []
nums.sort()
first_values = set()
for i, a in enumerate(nums):
    if i > 0 and a == nums[i-1]:
        continue
    l = i + 1
    r = len(nums)-1
    while l < r:
        sum = nums[i] + nums[l] + nums[r]
        if sum == 0:
            output.append([nums[i], nums[l], nums[r]])
            break
        elif sum > 0:
            r -= 1
        else:
            l += 1
print(output)