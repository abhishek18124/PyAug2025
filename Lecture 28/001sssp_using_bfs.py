from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # comment this out if graph is directed

s = 0  # source vertex / node

vis = [False] * n
q = deque()

vis[s] = True
q.append(s)

dis = [None] * n
dis[s] = 0

par = [None] * n
par[s] = -1

while q:
    cur = q.popleft()
    for ngb in adj[cur]:
        if not vis[ngb]:
            vis[ngb] = True
            q.append(ngb)
            dis[ngb] = dis[cur] + 1
            par[ngb] = cur

for i in range(n):
    print(f"dis({i}) = {dis[i]}")
print()


for i in range(n):
    print(f"par({i}) = {par[i]}")

d = 8  # destination vertex

# constructing the path from src to dst

path = []

cur = d

while par[cur] != -1:
    path.append(cur)
    cur = par[cur]

path.append(cur)
path.reverse()
print(path)
