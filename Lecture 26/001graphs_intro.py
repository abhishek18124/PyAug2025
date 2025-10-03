n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # comment this out if you are working with directed graphs

for i in range(n):
    print(f"ngb({i}) : ", end=" ")
    for ngb in adj[i]:
        print(ngb, end=" ")
    print()
