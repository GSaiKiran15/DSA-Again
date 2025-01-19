from typing import Counter
s = "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj"
h = Counter(s)
output = 0
for i in h:
    if h[i] % 2 == 0:
        output += 2
    else:
        output += 1
print(output)