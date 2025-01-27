pattern = "abba"
s = "dog cat cat dog"

h_p = {}
h_s = {}

for i, j in zip(pattern, s.split()):
    if (i in h_p and h_p[i] != j) or (j in h_s and h_s[j] != i):
        print(False)
    else:
        h_p[i] = j
        h_s[j] = i
    print(h_p, h_s)
print(True)
