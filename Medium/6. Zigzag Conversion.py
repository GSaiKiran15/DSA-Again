s = "PAYPALISHIRING" 
numRows = 3
if numRows == 1: print(s)
res = ""
for r in range(numRows):
    increment = (numRows - 1) * 2
    for i in range(r, len(s), increment):
        res += s[i]
        if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
            res += s[i + increment - 2 * r]
print(res)