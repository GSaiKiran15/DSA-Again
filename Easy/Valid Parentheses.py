s = "(])"
parentheses = {
    "}" : "{",
    "]" : "[",
    ")": "("
}

stack = []

for i,j in enumerate(s):
    if j in parentheses and not stack:
        print(False)
        break
    elif j in parentheses:
        if parentheses[j] == stack[-1]:
            stack.pop()
    else:
        stack.append(j)
print(True if not stack else False)