def search_matrix(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:

        if matrix[row][col] == target:
            return True

        elif matrix[row][col] > target:
            col -= 1

        else:
            row += 1

    return False


matrix = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

print(search_matrix(matrix, 5))