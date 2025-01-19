s = "))()))"
locked = "010100"
stack = []
i = 0
while i <= len(s)-1:
    if s[i] == "(" or (s[i] == ")" and locked[i] == "0"):
        if s[i+1] == ")" or (s[i+1] == "(" and locked[i+1] == "0"):
            i += 2
        else:
            print(False)
            break
    else:
        print(False)
        break
print(True)       
        