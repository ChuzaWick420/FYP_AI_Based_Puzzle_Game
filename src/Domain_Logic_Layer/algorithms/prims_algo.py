# Source: https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

def prims_algorithm(graph):

    nodes_count = graph.getNodesCount()
    old_adj = graph.getAdjMatrix()

    in_mst = [False] * nodes_count
    key_values = [float('inf')] * nodes_count
    parents = [-1] * nodes_count

    key_values[0] = 0  # Starting vertex

    for _ in range(nodes_count):
        u = min(
            (v for v in range(nodes_count) if not in_mst[v]),
            key=lambda v: key_values[v]
        )

        in_mst[u] = True

        for v in range(nodes_count):
            if (
                0 < old_adj[u][v] < key_values[v]
                and not in_mst[v]
            ):
                key_values[v] = old_adj[u][v]
                parents[v] = u

    new_adj_matrix = [
        [0] * nodes_count for _ in range(nodes_count)
    ]

    for v in range(1, nodes_count):
        u = parents[v]
        w = old_adj[u][v]
        new_adj_matrix[u][v] = w
        new_adj_matrix[v][u] = w  # undirected

    return new_adj_matrix

