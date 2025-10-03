# time : O(mn)
# space: O(n) due to dp[]


def f_bottomup_space_optimised(grid: list[list[int]], m: int, n: int) -> int:
    dp = [None] * n

    for i in range(m - 1, -1, -1):  # start=m-1 end=-1 step=-1 i.e. m-1 to 0
        for j in range(n - 1, -1, -1):  # start=n-1 end=-1 step=-1 i.e. n-1 to 0
            if i == m - 1 and j == n - 1:
                dp[j] = grid[i][j]
            elif i == m - 1:
                dp[j] = grid[i][j] + dp[j + 1]
            elif j == n - 1:
                dp[j] = grid[i][j] + dp[j]
            else:
                dp[j] = grid[i][j] + min(dp[j + 1], dp[j])

    # at this point of time dp[] holds the values of the 0th row

    return dp[0]  # at the 0th index of dp[] we store f(0, 0)


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
m = len(grid)
n = len(grid[0])

print(f_bottomup_space_optimised(grid, m, n))
