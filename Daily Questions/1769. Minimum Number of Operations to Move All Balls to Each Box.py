boxes = "001011"
res = [0] * len(boxes)
balls, moves = 0,0
for i in range(len(boxes)):
    res[i] = balls + moves
    moves += balls
    balls += int(boxes[i])
balls, moves = 0,0
for i in reversed(range(len(boxes))):
    res[i] += balls + moves
    moves += balls
    balls += int(boxes[i])
print(res)