t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0

    for k in range(n):
        s = 0
        for i in range(n):
            if i == k:
                s += a[i] + b[i]
            else:
                if a[i] > b[i]:
                    s += a[i]
                else:
                    s += b[i]
        if s > ans:
            ans = s

    print(ans)
