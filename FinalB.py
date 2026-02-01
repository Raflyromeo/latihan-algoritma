def dfs(graph, start, visited, reachable):
    visited[start] = True
    reachable.add(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, reachable)

def main():
    n, m = map(int, input().split())
    s = int(input())

    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited1 = [False] * (n + 1)
    reachable_from_capital = set()
    dfs(graph, s, visited1, reachable_from_capital)

    visited2 = [False] * (n + 1)
    can_return_to_capital = set()
    dfs(reverse_graph, s, visited2, can_return_to_capital)

    bidirectional_connected = reachable_from_capital & can_return_to_capital
    print(len(bidirectional_connected))

if __name__ == "__main__":
    main()
