nums1 = [0]
m = 0
nums2 = [2,5,6]
n = 3
index = -1
while m > 0 and n > 0:
    if nums1[m-1] <= nums2[n-1]:
        nums1[index] = nums2[n-1]
        index -= 1
        n -= 1
    elif nums1[m-1] > nums2[n-1]:
        nums1[index] = nums1[m-1]
        index -= 1
        m -= 1
print(nums1)