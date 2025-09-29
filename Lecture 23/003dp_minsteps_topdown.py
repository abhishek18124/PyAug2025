import sys

# time : O(n)
# space: O(n) due to function call stack and dp[]


def f_topdown(n: int, dp: list[int]) -> int:
    # lookup

    if dp[n] != -1:
        # you've already solved f(n), reuse the result
        return dp[n]

    # base case
    if n == 1:
        # f(1) : find min. steps required to reduce 1 to 1
        dp[n] = 0
        return dp[n]

    # recursive case

    # f(n) = finds the min steps required to reduce n to 1

    # decide the next operation

    # option 1: reduce n to n-1

    op1 = f_topdown(n - 1, dp)

    # option 2: reduce n to n/2 assuming n%2 is zero

    op2 = sys.maxsize
    if n % 2 == 0:
        op2 = f_topdown(n // 2, dp)

    # option 3: reduce n to n/3 assuming n%3 is zero

    op3 = sys.maxsize
    if n % 3 == 0:
        op3 = f_topdown(n // 3, dp)

    dp[n] = 1 + min(op1, op2, op3)
    return dp[n]


n = int(input())
dp = [-1] * (n + 1)  # dp[0] is not used
print(f_topdown(n, dp))
