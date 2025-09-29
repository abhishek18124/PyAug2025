cnt1 = 0
cnt2 = 0


# time : O(2^n)
# space: O(n) due to fn call stack


def f(n: int) -> int:
    global cnt1
    cnt1 += 1

    # base case

    if n == 0 or n == 1:
        return n

    # recursive case

    return f(n - 1) + f(n - 2)


# time : O(n)
# space: O(n) due to fn call stack and dp[]


def f_topdown(n: int, dp: list[int]) -> int:
    global cnt2
    cnt2 += 1

    # lookup

    if dp[n] != -1:
        # you've solved f(n) previously, reuse the result
        return dp[n]

    # base case

    if n == 0 or n == 1:
        dp[n] = n
        return dp[n]

    # recursive case

    dp[n] = f_topdown(n - 1, dp) + f_topdown(n - 2, dp)
    return dp[n]


# time : O(n)
# space : O(n) due to dp[]


def f_bottomup(n: int) -> int:
    dp = [None] * (n + 1)
    dp[0] = 0  # at the 0th index of dp[] we store f(0)
    dp[1] = 1  # at the 1st index of dp[] we store f(1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]  # at the nth index of dp[] we store f(n)


# time : O(n)
# space: O(1)


def f_bottomup_space_optimised(n: int) -> int:
    if n == 0 or n == 1:
        return n

    a = 0  # 0th fib. no.
    b = 1  # 1st fib. no.

    i = 1
    while i <= n - 1:
        c = a + b
        a = b
        b = c
        i += 1

    return c


n = int(input())
print(f(n))

dp = [-1] * (n + 1)
print(f_topdown(n, dp))

print(cnt1)
print(cnt2)

print(f_bottomup(n))

print(f_bottomup_space_optimised(n))
