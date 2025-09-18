arr = [5, 3, 6, 7, 2, 1, 4]
n = len(arr)

stk = []  # monotonic stk
ans = []

for i in range(n - 1, -1, -1):
    # find the nearest greater element to the right of arr[i]
    while len(stk) != 0 and stk[-1] <= arr[i]:
        stk.pop()

    if len(stk) == 0:
        # arr[i] doesn't have any greater elements to its right
        ans.append(-1)
    else:
        # whatever is at the top of the stack if the nearest
        # greater element to the right of arr[i]
        ans.append(stk[-1])

    stk.append(arr[i])

# print(ans[::-1]) # creates a shallow copy of ans

ans.reverse()  # reverses the list in-place

print(ans)
