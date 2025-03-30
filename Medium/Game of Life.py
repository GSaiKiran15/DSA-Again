board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(board)
m = len(board)
n = len(board[0])
count = 0
zero_indices = set()
one_indices = set()
for i in range(len(board)):
    for j in range(len(board[i])):
        one_count = 0
        zero_count = 0
        directions = [(i-1, j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
        for direction in directions:
            if (direction[0] >= 0 and direction[1] >= 0) and (direction[0] <= m-1 and direction[1] <= n-1):
                if board[direction[0]][direction[1]] == 1:
                    one_count += 1
                elif board[direction[0]][direction[1]] == 0:
                    zero_count += 1
            else:
                continue
        if board[i][j] == 1:
            if one_count < 2 or one_count > 3:
                zero_indices.add((i,j))
        else:
            if one_count == 3:
                one_indices.add((i,j))
for i in zero_indices:
    board[i[0]][i[1]] = 0
for i in one_indices:
    board[i[0]][i[1]] = 1
print(board)

                
            
        