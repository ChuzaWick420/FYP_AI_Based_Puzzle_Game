# Source: https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

def prims_algorithm(graph):
    in_mst = [False] * graph.size
    key_values = [float('inf')] * graph.size
    parents = [-1] * graph.size

    key_values[0] = 0  # Starting vertex

    print("Edge \tWeight")
    for _ in range(graph.size):
        u = min((v for v in range(graph.size) if not in_mst[v]), key=lambda v: key_values[v])

        in_mst[u] = True

        if parents[u] != -1:  # Skip printing for the first vertex since it has no parent
            print(f"{graph.vertex_data[parents[u]]}-{graph.vertex_data[u]} \t{graph.adj_matrix[u][parents[u]]}")

        for v in range(graph.size):
            if 0 < graph.adj_matrix[u][v] < key_values[v] and not in_mst[v]:
                key_values[v] = graph.adj_matrix[u][v]
                parents[v] = u
