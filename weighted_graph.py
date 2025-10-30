def get_vertices(rows, columns):
    vertices = []
    id = 0
    while (id < rows * columns):
        vertices.append(id)
        id = id + 1
    return vertices

def get_edges(rows, columns, vertices):
    # Make Grid
    row = [0] * columns
    grid = [row] * rows

    # NOTE: DEBUG - Checking Whole Vertex Map
    print(vertices)

    # Populate Grid
    for i in range(rows * columns):
        row_index = int(i / rows)
        column_index = i % columns

        # NOTE: DEBUG INFORMATION
        # WARN: GRID IS NOT CORRECTLY POPULATED, SOMETHING IS GOOPHI FOR SURE
        print("Loop Index: ", i)
        print("Row Index: ", row_index)
        print("Columns Index: ", column_index)
        print("Vertex ID: ", vertices[i])
        grid[row_index][column_index] = vertices[i]

    # Populate Grid
    # for i in range(rows):
    #     for j in range(columns):
    #         grid[i][j] = vertices[j + (columns * i)]

    # debug
    print("Grid: ", grid)
    return grid

class Weighted_Graph:
    def __init__(self, rows, columns):
        self.vertex = get_vertices(rows, columns)
        self.grid = get_edges(rows, columns, self.vertex)

    # Edge = ((v1, v2), weight)

    # Debug
    def print_vertex_count(self):
        print(self.vertex)

    # def print_grid(self):
    #     print(self.grid)
    #
