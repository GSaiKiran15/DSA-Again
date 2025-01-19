A = [1,3,2,4]
B = [3,1,2,4]
s = set()
output = []
for i, (a,b) in enumerate(zip(A,B)):
    if a not in s:
        s.add(a)