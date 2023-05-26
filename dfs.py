#DFS code

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(graph, root):
    if root not in visited:
        visited.add(root)
        print (root, end=' ')
        for i in graph[root]:
            dfs(graph, i)

# Driver Code
dfs(graph, 'A')