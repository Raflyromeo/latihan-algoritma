q = int(input())

for _ in range(q):
    s = input().strip()
    t = input().strip()

    ok = False

    for k in range(len(t) + 1):
        a = t[:k]
        b = t[k:]

        i = 0
        for ch in s:
            if i < len(a) and ch == a[i]:
                i += 1
        if i < len(a):
            continue

        j = len(b) - 1
        for ch in s[::-1]:
            if j >= 0 and ch == b[j]:
                j -= 1
        if j >= 0:
            continue

        ok = True
        break

    if ok:
        print("YES")
    else:
        print("NO")
