#BFS code:

graph = {
  'A' : ['B','C'],
  'B' : ['A','D', 'E'],
  'C' : ['A','F'],
  'D' : ['B'],
  'E' : ['B','F'],
  'F' : ['C','E']
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(graph, root):
  visited.append(root)
  queue.append(root)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for i in graph[s]:
      if i not in visited:
        visited.append(i)
        queue.append(i)


# Driver Code
bfs(graph, 'A')





