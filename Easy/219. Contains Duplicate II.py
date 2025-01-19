nums = [1,2,3,1]
k = 3
h = {}
for i, j in enumerate(nums):
    if j not in h:
        h[j] = i
    elif j in h and (i - h[j]) <= k:
        print(True)
    elif j in h:
        h[j] = i
print(False)