import heapq

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g[b].append((a, w))

dist = [10**18] * (n + 1)
par = [-1] * (n + 1)

h = []
heapq.heappush(h, (0, 1))
dist[1] = 0

while h:
    d, u = heapq.heappop(h)
    if d != dist[u]:
        continue
    for v, w in g[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            par[v] = u
            heapq.heappush(h, (dist[v], v))

if dist[n] == 10**18:
    print(-1)
else:
    ans = []
    cur = n
    while cur != -1:
        ans.append(cur)
        cur = par[cur]
    ans.reverse()
    print(*ans)
