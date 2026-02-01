n, L = map(int, input().split())
x = list(map(int, input().split()))
p = list(map(int, input().split()))

min_cost = float('inf')

for i in range(n):
    jarak = L - x[i]
    if jarak < 0:
        continue
    cost = jarak * p[i]
    if cost < min_cost:
        min_cost = cost

if min_cost == float('inf'):
    print("No solution")
else:
    print(int(min_cost))
