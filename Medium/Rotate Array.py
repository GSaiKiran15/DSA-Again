nums = [1,2,3,4,5,6,7,8, 9]
k = 3

k = k % len(nums)
nums = nums[-k:] + nums[:-k]

# for _ in range(k):
#     nums.insert(0, nums[-1])
#     nums.pop(-1)

print(nums)