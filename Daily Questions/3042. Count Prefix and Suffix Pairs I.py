words = ["a","abb"]
res = 0
for i in range(len(words)):
    for j in range(i+1, len(words)):
        if len(words[j]) < len(words[i]):
            continue
        print(words[j][:len(words[i])], words[j][:len(words[i])])
        if words[j][:len(words[i])] == words[i] and words[j][-len(words[i]):] == words[i]:
            res += 1
print(res)