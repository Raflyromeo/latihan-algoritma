N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = [1e9]
def f(i, t, n):
    if i == N: ans[0] = min(ans[0], n) if t == K else ans[0]; return
    f(i+1, t+A[i], n)
    f(i+1, t-A[i], n+1)
f(0, 0, 0)
print(-1 if ans[0] == 1e9 else int(ans[0]))