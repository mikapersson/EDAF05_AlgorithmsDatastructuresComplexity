import sys
from read_create import read_create
from edge import *
from find_path import find_path
from node import Node

""" Solution to lab 6 """

# SETUP
N, M, C, P = list(map(int, sys.stdin.readline().replace('\n', '').split(' ')))  # read input

edges, P_edges = read_create(M, P)

source = 0  # source node index
sink = N-1  # sink node index
graph = {}  # dictionary representation of graph
max_flow = 0

# solution starts at row X


def ford_fulkerson(G, s, t):
    """Finds the maximal flow from s to t in G"""

    # create residual graph, hur? en kopia av G? kanske...  hur mycket flöde kan jag ha bakåt?
    source_node = G[s]
    if t in G:
        sink_node = G[t]
    else:
        return 0

    path_exists, path_edges, delta = find_path(G, source_node, sink_node)
    while path_exists:  # while there is a path that isn't clogged up

        break

    return 0


# SOLUTION
while max_flow < C:
    """We construct the graph G 'backwards' with respect to P_list until we are above C capacity"""

    new_edge_index = P_edges.pop()
    new_edge = edges[new_edge_index]

    from_index = new_edge.destination1
    to_index = new_edge.destination2

    # rimligt?
    if from_index not in graph:
        new_city = Node(from_index)
        new_city.edges.append(new_edge)
        graph[from_index] = new_city
    else:
        graph[from_index].edges.append(new_edge)

    if to_index not in graph:
        new_city = Node(to_index)
        new_city.edges.append(new_edge.reverse())
        graph[to_index] = new_city  # undirected graph
    else:
        graph[to_index].edges.append(new_edge.reverse())

    max_flow = ford_fulkerson(graph, source, sink)  # find maximal flow with Ford-Fulkersons algorithm


print(len(P_edges), max_flow)  # len(P_edges) contain how many routes we didn't have to use (#removed edges)


'''
FRÅGOR
- vad vill jag att BFS på rad 25 ska returnera? -> (bool om man hittade path, lista på kanter, delta)?
'''
