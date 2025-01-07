strs = ["flower","flow","flight"]
output = ""
i = 0
length = min(len(strs[0]), len(strs[1]))
while i <= len(strs)-2:
    for j in range(len(min(strs[i], strs[i+1]))):
        if strs[i][j] == strs[i+1][j]:
            output