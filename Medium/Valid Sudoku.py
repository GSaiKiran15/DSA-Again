import collections
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

cols = collections.defaultdict(set)
rows = collections.defaultdict(set)
squares = collections.defaultdict(set)

for r in range(9):
    for c in range(9):
        if board[r][c] == ".":
            continue
        elif (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
            print(False)
        cols[c].add(board[r][c])
        rows[r].add(board[r][c])
        squares[(r // 3, c // 3)].add(board[r][c])
print(True)
    

# #check rows
# for row in board:
#     row_set = set()
#     for i in row:
#         if i == ".":
#             continue
#         elif 0 > int(i) or int(i) > 10 or int(i) in row_set:
#             print(False)
#         else:
#             row_set.add(int(i))

# # check columns
# for i in range(len(board)):
#     column_set = set()
#     for j in range(len(board)):
#         if board[j][i] == ".":
#             continue
#         elif int(board[j][i]) < 0 or int(board[j][i]) > 10 or int(board[j][i]) in column_set:
#             print(False)
#         else:
#             column_set.add(int(board[j][i]))

# multiples = [0,3,6,9]

# for i in range(len(multiples)-1):
#     box_set = set()
#     for a in range(multiples[i], multiples[i+1]):
#         for b in range(multiples[i], multiples[i+1]):
#             print(board[a][b])
#     print("next box")
            # if board[a][b] in box_set:
            #     print(False)
            # else:
            #     box_set.add(board[a][b])
    # print(box_set)