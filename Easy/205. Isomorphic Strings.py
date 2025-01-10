s = "paper"
t = "title"
s_h = {}
t_h = {}

for i in range(len(s)):
    if s[i] not in s_h:
        s_h[s[i]] = t[i]
    if t[i] not in t_h:
        t_h[t[i]] = s[i]

for i in range(len(s)):
    print(s_h[s[i]], t_h[s_h[s[i]]])
    print(t_h[t[i]], s_h[t_h[t[i]]])
    # i == t_h[s_h[i]] 