import sys


# time : O(3^n)
# space: O(n) due to function call stack
def f(n: int) -> int:
    # base case
    if n == 1:
        # f(1) : find min. steps required to reduce 1 to 1
        return 0

    # recursive case

    # f(n) = finds the min steps required to reduce n to 1

    # decide the next operation

    # option 1: reduce n to n-1

    op1 = f(n - 1)

    # option 2: reduce n to n/2 assuming n%2 is zero

    op2 = sys.maxsize
    if n % 2 == 0:
        op2 = f(n // 2)

    # option 3: reduce n to n/3 assuming n%3 is zero

    op3 = sys.maxsize
    if n % 3 == 0:
        op3 = f(n // 3)

    return 1 + min(op1, op2, op3)


n = int(input())
print(f(n))
