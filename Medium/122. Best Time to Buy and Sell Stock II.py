prices = [1,2,3,4,5]
output = 0
for i in range(len(prices)-1):
    if prices[i] < prices[i+1]:
        output += prices[i+1] - prices[i]
print(output)
    