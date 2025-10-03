# time : O(2^n)
# space: O(n)


def f(p: list[int], i: int, j: int, y: int) -> int:
    # base case

    if i == j:  # y == n
        return y * p[i]

    # recursive case

    # f(i, j, y) = it is a fn that finds the max. profit we
    # can make from wines[i...j] s.t. we are in year y

    # decide for the yth year

    # option 1 : sell the ith bottle of wine

    # option 2 : sell the jth bottle of wine

    return max(y * p[i] + f(p, i + 1, j, y + 1), y * p[j] + f(p, i, j - 1, y + 1))


p = [2, 3, 5, 1, 4]
n = len(p)

print(f(p, 0, n - 1, 1))
