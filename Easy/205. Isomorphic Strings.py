from itertools import zip_longest

s = "paper"
t = "title"

print(len(set(s)) == len(set(t)) == len(set(zip_longest(s, t))))

# s_h = {}
# t_h = {}

# for i in range(len(s)):
#     if s[i] not in s_h:
#         s_h[s[i]] = t[i]
#     if t[i] not in t_h:
#         t_h[t[i]] = s[i]

# for i in range(len(s)):
#     print(s_h[s[i]], t_h[s_h[s[i]]])
#     print(t_h[t[i]], s_h[t_h[t[i]]])
#     # i == t_h[s_h[i]] 