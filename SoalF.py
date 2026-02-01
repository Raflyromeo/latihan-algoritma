n = int(input())
arr = list(map(int, input().split()))

seen = set()
for num in arr:
    if num in seen:
        print("YES")
        exit(0)
    seen.add(num)

print("NO")