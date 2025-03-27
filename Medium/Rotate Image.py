matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
l = len(matrix)
a = 1

for i in range(l):
    
    
    temp_list = []
    
    
    for j in range(0,l):
        
        
        temp_list.append(matrix[-(j+a)][i])
        
        
    matrix.append(temp_list)
    a += 1
    
    # temp_list = []
    
    
for _ in matrix:
    matrix.pop(0)
print(matrix)