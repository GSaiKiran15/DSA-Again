from typing import Counter


s = "bbcbaba"

left_set = set()
right_hash = Counter(s)
output = set()

for i in s[:-1]:
    right_hash[i] -= 1

    for c in left_set:
        if right_hash[c] > 0:
            output.add((i, c))
    
    left_set.add(i)
    
print(len(output), output)
    
    

# l = 0
# r = len(s) - 1

# palindromes = set()
# alphabets = set()
# while l < len(s) - 2:
#     if s[l] == s[r]:
#         if s[l] not in alphabets:
#             for i in range(l+1, r):
#                 palindromes.add(s[l]+s[i]+s[r])
#         alphabets.add(s[l])
#     if r >= l + 2:
#         r -= 1
#     else:
#         r = len(s) - 1
#         l += 1
# print(palindromes, len(palindromes))
# print(alphabets)