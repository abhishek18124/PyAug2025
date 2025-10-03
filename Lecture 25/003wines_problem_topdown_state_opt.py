# time : O(n^2)
# space: n^2 due dp[][][] + n due to fn call stack ~ O(n^2)


def f_topdown(p: list[int], i: int, j: int, dp: list[list[int]]) -> int:
    n = len(p)
    y = n - j + i

    # lookup
    if dp[i][j] != -1:
        return dp[i][j]

    # base case

    if i == j:  # y == n
        dp[i][j] = y * p[i]
        return dp[i][j]

    # recursive case

    # f(i, j) = it is a fn that finds the max. profit we
    # can make from wines[i...j] s.t. we are in year y

    # decide for the yth year

    # option 1 : sell the ith bottle of wine

    # option 2 : sell the jth bottle of wine

    dp[i][j] = max(
        y * p[i] + f_topdown(p, i + 1, j, dp),
        y * p[j] + f_topdown(p, i, j - 1, dp),
    )

    return dp[i][j]


p = [2, 3, 5, 1, 4]
n = len(p)

dp = [[-1] * n for _ in range(n)]

print(f_topdown(p, 0, n - 1, dp))
