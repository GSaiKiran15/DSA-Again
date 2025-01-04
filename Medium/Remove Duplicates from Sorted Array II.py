nums = [0,0,1,1,1,1,2,3,3]
i = 2
l = len(nums)
output = 0
while i < l:
    if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
        nums.pop(i)
        output += 1
    else:
        i += 1
    l = len(nums)
print(l, nums)
# for i in range(1,len(nums[:])):
# # i = 1
# # while index < len(nums):
#     if nums[i-1] == nums[i] and nums[i-2] == nums[i]:
#         nums[i] = nums[i+1]
#         index += 2
# print(index, nums)      