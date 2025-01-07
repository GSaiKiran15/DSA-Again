haystack = "a"
needle = "a"
pointer = 0
i = 0
for i in range(len(haystack)):
    print(haystack[i:len(needle)+i],needle)
    if haystack[i:len(needle)+i] == needle:
        print(i)
        
    