nums = [2,2,1,1,1,2,2]

nums.sort()
print(nums[len(nums)//2])

element = nums[0]
count = 0
for i in nums:
    if i == element:
        count += 1
    elif i != element:
        count -= 1
        if count == -1:
            element = i
            count = 1
print(element)
    