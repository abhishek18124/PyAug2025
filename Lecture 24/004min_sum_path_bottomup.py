# time : O(mn)
# space: O(mn) due to dp[][]


def f_bottomup(grid: list[list[int]], m: int, n: int) -> int:
    dp = [[None] * n for _ in range(m)]
    for i in range(m - 1, -1, -1):  # start=m-1 end=-1 step=-1 i.e. m-1 to 0
        for j in range(n - 1, -1, -1):  # start=n-1 end=-1 step=-1 i.e. n-1 to 0
            if i == m - 1 and j == n - 1:
                dp[i][j] = grid[i][j]
            elif i == m - 1:
                dp[i][j] = grid[i][j] + dp[i][j + 1]
            elif j == n - 1:
                dp[i][j] = grid[i][j] + dp[i + 1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])

    # for i in range(m):
    #     for j in range(n):
    #         print(dp[i][j], end=" ")
    #     print()
    # print()

    x, y = 0, 0

    while not (x == m - 1 and y == n - 1):
        print(x, y)
        if y + 1 < n and dp[x][y] == grid[x][y] + dp[x][y + 1]:
            y += 1
        else:
            x += 1

    print(x, y)  # print destn coordinates

    return dp[0][0]  # at the 0,0th index of dp[][] we store f(0, 0)


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
m = len(grid)
n = len(grid[0])

print(f_bottomup(grid, m, n))
