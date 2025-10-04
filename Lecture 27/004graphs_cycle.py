n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # comment this out if graph is directed

vis = [False] * n

# time : O(n + 2m) or O(V + 2E)
# space: O(n + n) i.e. O(n) due vis[] & fn call stack or O(V)


def dfs(u, par_u):
    vis[u] = True
    for v in adj[u]:
        if not vis[v]:
            if dfs(v, u):
                # you've found cycle in the subcomp of v
                # therefore you've found cycle in the comp of u
                return True
        else:
            # check if u to v is a backedge
            if par_u != v:
                # we've found a backedge
                # therefore we've found a cycle
                return True
    return False


flag = False  # assume no cycles present

for i in range(n):
    if not vis[i]:
        # make node i as src
        if dfs(i, -1):
            # cycle found in the component of node i
            # therefore graph is cyclic
            flag = True
            break

if flag:
    print("cycle found")
else:
    print("cycle not found")
