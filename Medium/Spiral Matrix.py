matrix = [[1,2,3],[4,5,6],[7,8,9]]

m = len(matrix)
n = len(matrix[0])
res = []
visited = set()
left = 0

def move_right(i,j):
    print("move right")
    next_j = 0
    for move in range(j,n):
        if (i,move) in visited:
            move_down(i+1,j)
        else:
            res.append(matrix[i][move])
            visited.add((i,move))
        next_j = move
    left += 1
    if len(res) == m*n:
        return res
    else:
        move_down(i+1, next_j)

def move_down(i,j):
    next_i = 0
    print("move down")
    for move in range(i,m):
        if (move,j) in visited:
            move_left(i,j-1)
        else:
            res.append(matrix[move][j])
            visited.add((move,j))
        next_i = move
    if len(res) == m*n:
        return res
    else:
        move_right(next_i, j)

def move_left(i,j):
    print("move left")
    for move in range(j-1,left-1, -1):
        if (i,move) in visited:
            move_right(i+1,j)
        else:
            res.append(matrix[i][move])
            visited.add((i,move))
    if len(res) == m*n:
        return res
    else:
        move_up()

def move_up(i,j):
    print("move up")
    for move in range():
        if (i,move) in visited:
            move_down(i+1,j)
        else:
            res.append(matrix[i][move])
            visited.add((i,move))
    if len(res) == m*n:
        return res

move_right(0,0)
