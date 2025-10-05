import heapq
import sys

INF = sys.maxsize

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))  # comment this out if graph is directed

s = 0  # src vertex

dis = [INF] * n
dis[s] = 0

expl = [False] * n  # to track explored status of nodes

min_heap = []  # to track unexplored nodes
for i, d in enumerate(dis):
    heapq.heappush(min_heap, (d, i))

# time : O(ElogV)
# space: O(V)

while min_heap:
    dis_cur, cur = heapq.heappop(min_heap)
    if dis_cur > dis[cur]:
        continue
    for ngb, edge_wt in adj[cur]:
        if not expl[ngb] and dis[ngb] > dis_cur + edge_wt:
            # edge b/w cur and ngb is tensed so relax
            dis[ngb] = dis_cur + edge_wt
            heapq.heappush(min_heap, (dis[ngb], ngb))
    expl[cur] = True

for i in range(n):
    print(f"dis({i}) = {dis[i]}")
