T = int(input())
res = []
for p in [2**i for i in range(19,-1,-1)]:
    if T >= p:
        res.append(str(p))
        T -= p
print(' '.join(res))