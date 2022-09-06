# Find the shortest path in a graph and print it as a sequence
# from S vertex to D vertex. Implement the Bellman-Ford algorithm.
# Input
# The input comes from the console.
#    On the first line, you will receive an integer – n – the number of nodes.
#    On the next line, you will receive an integer – e – the number of edges.
#    On the next e lines, you will receive an edge in the following format: "{from} {to} {weight}".
#    On the last two lines, you will receive source and destination nodes.
# Output
#    Print "Negative Cycle Detected" if detect a negative cycle.
#    Otherwise, print the shortest path separated by a space and the total distance.
# Input                             Output
# 6                                 1 2 4 3 6
# 8                                 7
# 1 2 8
# 1 3 10
# 2 4 1
# 3 6 2
# 4 3 -4
# 4 6 -1
# 6 5 -2
# 5 3 1
# 1
# 6
# -----------------------------------------------------------
# 4                                 Negative Cycle Detected
# 4
# 1 2 1
# 2 3 -1
# 3 4 -1
# 4 1 -1
# 1
# 4
