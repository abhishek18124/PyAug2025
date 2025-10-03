# time : O(n^3)
# space: n^3 due dp[][][] + n due to fn call stack ~ O(n^3)


def f_topdown(p: list[int], i: int, j: int, y: int, dp: list[list[list[int]]]) -> int:
    # lookup
    if dp[i][j][y] != -1:
        return dp[i][j][y]

    # base case

    if i == j:  # y == n
        dp[i][j][y] = y * p[i]
        return dp[i][j][y]

    # recursive case

    # f(i, j, y) = it is a fn that finds the max. profit we
    # can make from wines[i...j] s.t. we are in year y

    # decide for the yth year

    # option 1 : sell the ith bottle of wine

    # option 2 : sell the jth bottle of wine

    dp[i][j][y] = max(
        y * p[i] + f_topdown(p, i + 1, j, y + 1, dp),
        y * p[j] + f_topdown(p, i, j - 1, y + 1, dp),
    )

    return dp[i][j][y]


p = [2, 3, 5, 1, 4]
n = len(p)

dp = [[[-1] * (n + 1) for _ in range(n)] for _ in range(n)]

print(f_topdown(p, 0, n - 1, 1, dp))
