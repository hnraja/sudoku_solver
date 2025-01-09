def is_valid_move(grid, row, col, num):
    if num in grid[row]: return False
    if num in [grid[i][col] for i in range(9)]: return False
    corner_r, corner_c = row // 3, col // 3
    if num in [grid[3 * corner_r + i][3 * corner_c + j] for i in range(3) for j in range(3)]:
      return False
    return True

def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve(grid, row, col + 1): return True

        grid[row][col] = 0

    return False

grid = [[0, 9, 6, 0, 0, 5, 0, 0, 4],
        [0, 7, 1, 0, 3, 4, 9, 6, 0],
        [4, 0, 0, 9, 0, 2, 7, 3, 0],
        [0, 2, 0, 0, 9, 0, 3, 4, 6],
        [9, 0, 8, 3, 4, 0, 1, 2, 7],
        [6, 3, 0, 2, 7, 0, 0, 0, 8],
        [0, 4, 9, 1, 0, 0, 0, 0, 2],
        [7, 0, 0, 0, 0, 0, 0, 5, 0],
        [5, 6, 3, 4, 0, 7, 0, 0, 9]]


if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end="  ")
        print()
else:
    print("No solution")

