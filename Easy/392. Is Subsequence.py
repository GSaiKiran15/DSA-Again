s = "axc"
t = "ahbgdc"
a = 0
for i in t:
    if s[a] == i:
        a += 1
    if a == len(s):
        print(True)
print(False)