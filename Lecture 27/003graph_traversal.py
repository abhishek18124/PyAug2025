n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # comment this out if graph is directed

s = 0  # source vertex
vis = [False] * n

# time : O(n + 2m) or O(V + 2E)
# space: O(n + n) i.e. O(n) due vis[] & fn call stack or O(V)


def dfs(cur):
    vis[cur] = True
    print(cur, end=" ")
    for ngb in adj[cur]:
        if not vis[ngb]:
            dfs(ngb)


num = 0

for i in range(n):
    if not vis[i]:
        # make node i as src
        print(f"dfs({i}) : ", end=" ")
        dfs(i)
        print()
        num += 1

print(f"num of components = {num}")
