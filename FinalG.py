a, b, x, y = map(int, input().split())

if a > b:
    print(-1)
else:
    diff = b - a
    cost_add = diff * x
    cost_xor = y if diff == 1 else float('inf')
    print(min(cost_add, cost_xor))
