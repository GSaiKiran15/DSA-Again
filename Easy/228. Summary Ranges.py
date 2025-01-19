nums = [0,1,2,4,5,7]
output = []
s = f"{nums[0]}"
l = 0
r = 1
for i in range(len(nums)-1):
    if nums[r-1]+1 != nums[r]:
        if l != r-1:
            s += f"->{nums[r-1]}"
        output.append(s)
        l = r
        s = f"{nums[l]}"
    r += 1
    if r >= len(nums):
        if l != r-1:
            s += f"->{nums[r-1]}"
        output.append(s)
if l == len(nums) - 1:
    output.append(f"{nums[l]}")
else:
    output.append(f"{nums[l]}->{nums[-1]}")
print(output)
    
#Best Solution
    
result = []
if not nums:
    print(result)

start = nums[0]
for i in range(1, len(nums) + 1):
    if i == len(nums) or nums[i] != nums[i - 1] + 1:
        if start == nums[i - 1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[i - 1]}")
        if i < len(nums):
            start = nums[i]
print(result)