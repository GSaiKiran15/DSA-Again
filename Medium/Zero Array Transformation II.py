nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]
k = 0
for i in range(len(queries)):
    k += 1
    for j in range(queries[i][0], queries[i][1]+1):
        if nums[j] != 0:
            nums[j] -= queries[i][2]
            if nums[j] < 0:
                nums[j] = 0
    zero_counter = 0
    for i in nums:
        if i == 0:
            zero_counter += 1
    if zero_counter == len(nums):
        print(k)
        break
print(-1)
                        
        