import sys

# time : O(n)
# space: O(n) due to dp[]


def f_bottomup(n: int) -> int:
    dp = [None] * (n + 1)  # 0th index is not used
    dp[1] = 0  # at the 1st index of dp[] we store f(1)

    for i in range(2, n + 1):
        # dp[i] = f(i) = min steps required to reduce i to 1

        # decide the next operation

        # option 1 : reduce i to i - 1

        op1 = dp[i - 1]

        # option 2 : reduce i to i / 2 assuming i%2 is zero

        op2 = sys.maxsize
        if i % 2 == 0:
            op2 = dp[i // 2]

        # option 3 : reduce i to i / 3 assuming i%3 is zero

        op3 = sys.maxsize
        if i % 3 == 0:
            op3 = dp[i // 3]

        dp[i] = 1 + min(op1, op2, op3)

    return dp[n]  # at the nth index of dp[] we store f(n)


n = int(input())
print(f_bottomup(n))
