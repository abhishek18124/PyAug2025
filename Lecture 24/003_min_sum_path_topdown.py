# time : O(mn)
# space: (m+n) due to fn call stack + mn due to dp[][] ~ O(mn)


def f_topdown(
    grid: list[list[int]], m: int, n: int, i: int, j: int, dp: list[list[int]]
) -> int:
    # lookup
    if dp[i][j] != -1:
        # you've already solved f(i, j) so reuse the result
        return dp[i][j]

    # base case
    if i == m - 1 and j == n - 1:
        dp[i][j] = grid[i][j]
        return dp[i][j]

    # recursive case

    # f(i, j) = find the min sum path from i,jth cell to m-1,n-1th cell

    # decide the next step

    if j == n - 1:
        # we are in the last column
        dp[i][j] = grid[i][j] + f_topdown(grid, m, n, i + 1, j, dp)
        return dp[i][j]

    if i == m - 1:
        # we are in the last row
        dp[i][j] = grid[i][j] + f_topdown(grid, m, n, i, j + 1, dp)
        return dp[i][j]

    # option 1 : move right

    # option 2 : move down

    dp[i][j] = grid[i][j] + min(
        f_topdown(grid, m, n, i, j + 1, dp), f_topdown(grid, m, n, i + 1, j, dp)
    )
    return dp[i][j]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
m = len(grid)
n = len(grid[0])

dp = [[-1] * n for _ in range(m)]

print(f_topdown(grid, m, n, 0, 0, dp))
