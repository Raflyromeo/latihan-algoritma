from collections import deque

def solve(z, w, m):
    if z == w:
        return 0

    q = deque()
    q.append((z, 0))
    vis = set()

    while q:
        now, step = q.popleft()

        if now == w:
            return step

        if now in vis:
            continue
        vis.add(now)

        for i in range(2, m + 1):
            if now * i <= 1000000:
                q.append((now * i, step + 1))

        for i in range(2, m + 1):
            if now % i == 0:
                q.append((now // i, step + 1))

    return -1

t = int(input())
for _ in range(t):
    z, w, m = map(int, input().split())
    print(solve(z, w, m))
