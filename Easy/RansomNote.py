from typing import Counter

#Uses less memory and time

# if ransomNote in magazine: return True
# r = set(ransomNote)
# for i in r:
#     if ransomNote.count(i) > magazine.count(i):
#         return False
# return True

# Brute Force

ransomNote = "aa"
magazine = "ab"

r = Counter(ransomNote)
m = Counter(magazine)
print(r,m)
for i in ransomNote:
    if i in m:
        m[i] -= 1
    if i not in m or m[i] < 0:
        print(False)
        break
    
print(True)