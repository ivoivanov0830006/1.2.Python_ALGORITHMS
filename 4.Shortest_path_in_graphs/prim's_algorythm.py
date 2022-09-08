from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


    def __gt__(self, other):   # greater than....   or lower than
        return self.weight > other.weight


def prim(node, graph, forest, forest_edges):
    forest.add(node)

    pq = PriorityQueue()
    for edge in graph[node]:
        pq.put(edge)

        while not pq.empty():
            min_edge = pq.get()
            non_tree_node = -1

            if min_edge.first in forest and min_edge.second not in forest:
                non_tree_node = min_edge.second
            elif min_edge.second in forest and min_edge.first not in forest:
                non_tree_node = min_edge.first

            if non_tree_node == -1:
                continue

            forest.add(non_tree_node)
            forest_edges.append(min_edge)

            for edge in graph[non_tree_node]:
                pq.put(edge)


edges = int(input())

graph = {}

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(", ")]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

forest = set()
forest_edges = []

for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forest_edges)

for edge in forest_edges:
    print(f"{edge.first} - {edge.second}")


# If we have a weighted undirected graph, we can extract a sub-graph where all nodes
# (vertices) of the original graph are connected by edges without any cycles.
# This is referred to as a spanning tree. A minimum spanning tree (MST) is the spanning
# tree with the smallest weight (several MST could exist in some graphs).
# For example, a cable operator wants to connect its customers to a cable network.
# The homes of the customers are connected by streets (edges) with different
# lengths (weights). To find out how to connect all homes to its network most efficiently
# (least distance covered) you need to find the MST. One simple algorithm to find the
# MST of a given graph is Prim’s algorithm.
# Input
#   On the first line, you will receive e – an integer – number of edges that you have to read.
#   On the next e lines, you will receive an edge in the following format: "{firstNode}, {seconNode}, {weight}".
# Output
#   Print all edges part of the minimum spanning tree in the following format: "{first} - {second}".
#   The order of the output doesn’t matter.
# Input                           Output
# 11                              0 - 1
# 0, 2, 5                         1 - 3
# 2, 4, 7                         0 - 2
# 4, 5, 12                        2 - 4
# 0, 1, 4                         4 - 5
# 1, 3, 2                         6 - 7
# 0, 3, 9                         7 - 8
# 2, 3, 20
# 3, 4, 8
# 6, 7, 8
# 6, 8, 10
# 7, 8, 7
