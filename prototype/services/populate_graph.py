import random
import math

def index_1d_to_2d(index, size):
    # WARNING: 
    # Assumption:
    # index starts from 0 and first row and column are 0, not 1

    y = index // size
    x = index % size
    return x, y

def index_2d_to_1d(x, y, size):
    return y * size + x

def populate_graph(graph, size):

    one_dimensional_size = int(math.sqrt(size))

    for i in range(0, size):
        graph.add_vertex_data(i, str(i))

    for i in range(0, size):
        left_boundary =  int((i % one_dimensional_size)) == 0
        right_boundary = int((i + 1) % one_dimensional_size) == 0
        upper_boundary = int((i / one_dimensional_size)) < 1
        lower_boundary = int((i / one_dimensional_size) + 1) == one_dimensional_size

        max = 9
        min = 1

        coords = index_1d_to_2d(i, one_dimensional_size)

        x = coords[0]
        y = coords[1]

        if (not left_boundary):
            weight = min + int(random.random() * 10) % (max - min + 1)
            graph.add_edge(i, i - 1, weight)
        if (not right_boundary):
            weight = min + int(random.random() * 10) % (max - min + 1)
            graph.add_edge(i, i + 1, weight)
        if (not upper_boundary):
            weight = min + int(random.random() * 10) % (max - min + 1)
            graph.add_edge(i, index_2d_to_1d(x, y - 1, size), weight)
        if (not lower_boundary):
            weight = min + int(random.random() * 10) % (max - min + 1)
            graph.add_edge(i, index_2d_to_1d(x, y + 1, size), weight)
