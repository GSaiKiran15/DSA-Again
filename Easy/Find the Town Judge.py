from collections import defaultdict

n = 3
trust = [[1,2],[2,3]]

trusted = [0] * (n + 1)
for (a,b) in trust:
    trusted[a] -= 1
    trusted[b] += 1

for i in range(1, len(trusted)):
    if trusted[i] == n - 1:
        print(i)
print(-1)


incoming  = defaultdict(int)
outgoing = defaultdict(int)

for src, dst in trust:
    incoming[dst] += 1
    outgoing[src] += 1

for i in range(1, n+1):
    if outgoing[i] == 0 and incoming[i] == n-1:
        print(i)

print(-1)