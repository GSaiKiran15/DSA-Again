print(sum([1 for i in (str(bin(n))[2:]) if i=="1"])) #best space complexity

#best time complexity
output = 0
while n:
    output += n & 1
    n >>= 1
return output