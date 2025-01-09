numbers = [2,3,4]
target = 6

# Uses no extra memory

l, r = 0, len(numbers) - 1

while l<r:
    if numbers[l] + numbers[r] < target:
        l += 1
    elif numbers[l] + numbers[r] > target:
        r -= 1
    else:
        print([l+1, r+1])
        break

# Uses extra memory

# hash_map = {}
# for i, j in enumerate(numbers):
#     if j not in hash_map:
#         hash_map[j] = i
#     if j in hash_map:
#         if (target - j) in hash_map and hash_map[(target - j)] != i:
#             print([hash_map[target - j]+1, i + 1])
#             break
    
