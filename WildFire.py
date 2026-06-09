def wildfire(grid, i, j):
    # Check boundaries and stop if cell is not 1
    if (
        i < 0 or i >= len(grid) or
        j < 0 or j >= len(grid[0]) or
        grid[i][j] != 1
    ):
        return

    # Mark the current cell as burned/visited
    grid[i][j] = 2

    # Spread in four directions
    wildfire(grid, i + 1, j)  # down
    wildfire(grid, i - 1, j)  # up
    wildfire(grid, i, j + 1)  # right
    wildfire(grid, i, j - 1)  # left


matrix = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 0]
]

# Start wildfire from the top-left corner
wildfire(matrix, 0, 0)

# Count remaining trees (cells with value 1)
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            count += 1

print("Remaining trees:", count)
print(matrix)