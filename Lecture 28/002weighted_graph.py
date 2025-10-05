n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))  # comment this out if graph is directed

for i in range(n):
    print(f"ngb({i}) : ", end=" ")
    for ngb, wt in adj[i]:
        print(f"({ngb}, {wt}) ", end=" ")
    print()
