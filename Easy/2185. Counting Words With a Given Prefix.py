words = ["pay","attention","practice","attend"]
pref = "at"
count = 0
for i in words:
    if len(i) < len(pref):
        print(0)
    print(i[:len(pref)],pref)
    if i[:len(pref)] == pref:
        count += 1
print(count)