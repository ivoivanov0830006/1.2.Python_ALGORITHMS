from collections import deque

nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node == destination_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = deque()
node = destination_node
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(f"Shortest path length is: {len(path) - 1}")
print(*path, sep= " ")

# You will be given a graph from the console your task is to find the shortest path
# and print it back on the console. The first line will be the number of Nodes -
# N the second one the number of Edges - E, then on each E line the edge in form
# {destination} – {source}. On the last two lines, you will read the start node and the end node.
# Print on the first line the length of the shortest path and the second the path itself,
# see the examples below.
# Input                         Output
# 8                             Shortest path length is: 3 1 4 5
# 10
# 1 2
# 1 4
# 2 3
# 4 5
# 5 8
# 5 6
# 5 7
# 5 8
# 6 7
# 7 8
# 1
# 7
