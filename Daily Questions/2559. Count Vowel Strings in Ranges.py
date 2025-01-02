words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
output = []
words_with_values = [0]
vowels = "aeiou"
count = 0

for i in words:
    if i[0] in vowels and i[-1] in vowels:
        count += 1
    words_with_values.append(count)

for i in queries:
    output.append(words_with_values[i[1]+1] - words_with_values[i[0]])

print(output)
        