import random

def get_vertices(rows, columns):
    vertices = []
    id = 0
    while (id < rows * columns):
        vertices.append(id)
        id = id + 1
    return vertices

def get_grid(rows, columns, vertices):
    # Make Grid
    grid = [[0] * columns for _ in range(rows)]

    # Populate Grid
    for i in range(rows * columns):
        row_index = i // columns
        column_index = i % columns
        grid[row_index][column_index] = vertices[i]

    return grid

def get_edges(rows, columns, grid):
    edges = []
    for i in range(rows):
        for j in range(columns):
            row_index = i
            column_index = j

            # Up
            if(not (row_index - 1 < 0)):
                pair = {grid[i][j], grid[row_index - 1][j]}
                if (not pair in edges):
                    edges.append(pair)

            # Right
            if (not (column_index + 1 >= columns)):
                pair = {grid[i][j], grid[i][j + 1]}
                if (not pair in edges):
                    edges.append(pair)

            # Down
            if(not (row_index + 1 >= rows)):
                pair = {grid[i][j], grid[row_index + 1][j]}
                if (not pair in edges):
                    edges.append(pair)

            # Left
            if (not (column_index - 1 < 0)):
                pair = {grid[i][j], grid[i][j - 1]}
                if (not pair in edges):
                    edges.append(pair)

    print(len(edges))
    return edges

class Weighted_Graph:
    def __init__(self, rows, columns):
        self.vertices = get_vertices(rows, columns)
        self.grid = get_grid(rows, columns, self.vertices)
        self.edges = get_edges(rows, columns, self.grid)

    # Debug
    def print_vertex_count(self):
        print(self.vertices)

    def print_grid(self):
        print(self.grid)

