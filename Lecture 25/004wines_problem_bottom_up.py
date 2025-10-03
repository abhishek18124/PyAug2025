# time : O(n^2)
# space: O(n^2)
# [HW] space can be optimised to O(n)


def f_bottomup(p: list[int], n: int) -> int:
    dp = [[None] * n for _ in range(n)]

    for i in range(n):
        # j = i
        # y = n
        # dp[i][j] = y * p[i]
        dp[i][i] = n * p[i]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            y = n - j + i
            dp[i][j] = max(y * p[i] + dp[i + 1][j], y * p[j] + dp[i][j - 1])

    return dp[0][n - 1]  # at the 0,n-1th index of dp[][] we store f(0, n-1)


p = [2, 3, 5, 1, 4]
n = len(p)

print(f_bottomup(p, n))
