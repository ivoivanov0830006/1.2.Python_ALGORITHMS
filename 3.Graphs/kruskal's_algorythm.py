class Edge:
    def __init__(self, first, second, weight):
        self.weight = weight
        self.second = second
        self.first = first


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


edges = int(input())
graph = []

max_node = float("-inf")
for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(", ")]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node)

parent = [num for num in range(max_node + 1)]
forest = []
for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)
    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest.append(edge)

for edge in forest:
    print(f"{edge.first} - {edge.second}")


# If we have a weighted undirected graph, we can extract a sub-graph where all nodes
# (vertices) of the original graph are connected by edges without any cycles.
# This is referred to as a spanning tree. A minimum spanning tree (MST) is the
# spanning tree with the smallest weight (several MST could exist in some graphs).
# For example, a cable operator wants to connect its customers to a cable network.
# The homes of the customers are connected by streets (edges) with different lengths
# (weights). To find out how to connect all homes to its network most efficiently
# (least distance covered) you need to find the MST. One simple algorithm to find
# the MST of a given graph is Kruskal’s algorithm.
# Input
#   On the first line you will receive e – an integer – number of edges that you have to read.
#   On the next e lines, you will receive an edge in the following format:
#       "{firstNode}, {secondNode}, {weight}".
# Output
#   Print all edges part of the minimum spanning tree in the following format: "{first} - {second}".
#   The order of the output doesn’t matter.
# Input                                 Output
# 11                                    3 - 5
# 0, 3, 9                               0 - 5
# 0, 5, 4                               0 - 8
# 0, 8, 5                               1 - 7
# 1, 4, 8                               6 - 8
# 1, 7, 7                               1 - 4
# 2, 6, 12                              2 - 6
# 3, 5, 2
# 3, 6, 8
# 3, 8, 20
# 4, 7, 10
# 6, 8, 7
