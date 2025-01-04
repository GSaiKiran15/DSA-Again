nums = [2,2,1,1,1,2,2]

count = 1
res = nums[0]

for i in range(1, len(nums)):
    if nums[i] == res:
        count += 1
    else:
        count -= 1
    if count == 0:
        res = nums[i]
        count = 1
print(res)