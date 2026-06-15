def dfs(node, result, visited, adj):
    visited[node] = 1
    result.append(node)
    for n in adj[node]:
        if visited[n] == 0:
            dfs(n, result, visited, adj)



adjacent_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = {node: 0 for node in adjacent_list}
result = []

dfs('A', result, visited, adjacent_list)
print(result)
