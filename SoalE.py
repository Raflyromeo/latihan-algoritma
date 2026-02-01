n, m = map(int, input().split())
s, t = map(int, input().split())
p = list(range(n + 1))

def f(x):
    if p[x] != x:
        p[x] = f(p[x])
    return p[x]

for _ in range(m):
    u, v = map(int, input().split())
    p[f(u)] = f(v)

print("YES" if f(s) == f(t) else "NO")
