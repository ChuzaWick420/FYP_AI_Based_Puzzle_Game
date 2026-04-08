import pygame
from prototype.Domain_Logic_Layer.algorithms.prims_algo import prims_algorithm
from prototype.Domain_Logic_Layer.entities.Graph import Graph
from prototype.Service_Layer.maze_generator import generate_maze
from prototype.Service_Layer.mst_to_presentation_grid import mst_to_presentation_grid

size = 9 * 9

g = Graph(size)
# Debug
print("Post Creation: ", g.adj_matrix)

adjacent_matrix = prims_algorithm(g)
g.adj_matrix = adjacent_matrix

# Debug
print("Post Algorithm: ", g.adj_matrix)

grid = mst_to_presentation_grid(g)

# Debug
print("Presentation: ")
for row in grid:
    print(row)

visual = generate_maze(grid)

# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((300, 300))

# Set the caption of the screen
pygame.display.set_caption('Geeksforgeeks')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# game loop
while running:
  
# for loop through the event queue  
    for event in pygame.event.get():
    
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False

    visual.draw(screen)
    pygame.display.flip()

pygame.quit()
