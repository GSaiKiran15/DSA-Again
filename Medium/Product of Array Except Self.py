def productExceptSelf(self, nums: List[int]) -> List[int]:
    output = [1] * len(nums)
    prefix = 1
    post = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]
    for i in range(len(nums)-1, -1, -1):
        output[i] = output[i] * post
        post = post * nums[i]
    return output