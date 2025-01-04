prices = [7,1,5,3,6,4]

max_profit = 0
left = prices[0]

for i in prices:
    temp_profit = i - left
    max_profit = max(temp_profit, max_profit)
    left = min(left, i)
print(max_profit)

# left = 0
# right = 1
# max_profit = 0

# while right <= len(prices)-1:
#     if prices[left] > prices[right]:
#         left = right
#     elif prices[left] < prices[right]:
#         max_profit = max(max_profit, prices[right] - prices[left])
#     right += 1
# print(max_profit)