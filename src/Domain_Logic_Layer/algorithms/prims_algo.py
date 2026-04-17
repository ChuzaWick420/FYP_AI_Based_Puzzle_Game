# Source: https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

def prims_algorithm(graph):
    in_mst = [False] * graph.total_nodes
    key_values = [float('inf')] * graph.total_nodes
    parents = [-1] * graph.total_nodes

    key_values[0] = 0  # Starting vertex

    for _ in range(graph.total_nodes):
        u = min(
            (v for v in range(graph.total_nodes) if not in_mst[v]),
            key=lambda v: key_values[v]
        )

        in_mst[u] = True

        for v in range(graph.total_nodes):
            if (
                0 < graph.adj_matrix[u][v] < key_values[v]
                and not in_mst[v]
            ):
                key_values[v] = graph.adj_matrix[u][v]
                parents[v] = u

    new_adj_matrix = [
        [0] * graph.total_nodes for _ in range(graph.total_nodes)
    ]

    for v in range(1, graph.total_nodes):
        u = parents[v]
        w = graph.adj_matrix[u][v]
        new_adj_matrix[u][v] = w
        new_adj_matrix[v][u] = w  # undirected

    return new_adj_matrix

