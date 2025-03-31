def spiralOrder(matrix):
    if not matrix:
        return []

    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # Move right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # Move down
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # Move left
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # Move up
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res

# Define the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Call the function and print the result
print(spiralOrder(matrix))
