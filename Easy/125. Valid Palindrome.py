s = "A man, a plan, a canal: Panama"
output = ""
for i in s:
    if i.isalnum():
        output += i.lower()
print(output == output[::-1])
