matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

#Better Solution

zero_row = []
zero_col = []
m = len(matrix[0])
n = len(matrix)
print(m,n)
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zero_row.append(i)
            zero_col.append(j)
for i in zero_row:
    for j in range(m):
        matrix[i][j]=0
for i in zero_col:
    for j in range(n):
        matrix[j][i]=0

# My solution

m = len(matrix)
n = len(matrix[0])
coordinates = set()
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            for z in range(m):
                coordinates.add((z,j))
            for x in range(n):
                coordinates.add((i,x))
for i in coordinates:
    matrix[i[0]][i[1]] = 0
print(matrix)
    
                