words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
output = set()
count = 0
words_string = ','.join(words1)
for i in words2:
    l = 0
    r = len(i)-1
    while r < len(words1[count]):
        if words_string[l:r+1] == i:
            output.add(words1[count])
        if words_string[l:r+1][-1] == ",":
            count += 1
            l = r + 1
            r += 2
            continue
        r += 1
        l += 1
print(output)
            
    