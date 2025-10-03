def f(grid: list[list[int]], m: int, n: int, i: int, j: int) -> int:
    # base case
    if i == m - 1 and j == n - 1:
        return grid[i][j]

    # recursive case

    # f(i, j) = find the min sum path from i,jth cell to m-1,n-1th cell

    # decide the next step

    if j == n - 1:
        # we are in the last column
        return grid[i][j] + f(grid, m, n, i + 1, j)

    if i == m - 1:
        # we are in the last row
        return grid[i][j] + f(grid, m, n, i, j + 1)

    # option 1 : move right

    # option 2 : move down

    return grid[i][j] + min(f(grid, m, n, i, j + 1), f(grid, m, n, i + 1, j))


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
m = len(grid)
n = len(grid[0])

print(f(grid, m, n, 0, 0))
