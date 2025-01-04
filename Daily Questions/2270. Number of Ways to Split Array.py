nums = [2,3,1,0]
total = 0
sub_count = 0
output = 0
for i in nums:
    total += i
for i in range(len(nums)-1):
    sub_count += nums[i]
    if sub_count >= total - sub_count:
        output += 1
print(output)