import pygame
from queue import PriorityQueue
import math
from A_sharp import *
# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the colors
black = (0, 0, 0)
gray = (128, 128, 128)
red = (255, 0, 0)
green = (0, 255, 0)

# Define the grid size and node size
grid_size = 10
node_size = grid_size // 2

# Define the initial positions of the vehicle and the target
vehicle_pos = [19, 19]
target_pos = [14, 10]
obstacles_list = [[20,18],[21,18],[22,18],[23,18]]

# Define the vehicle speed and delay between key presses
vehicle_speed = 1
key_delay = 100 # milliseconds

# Define timers to keep track of the time since the last key press
last_left_key_time = 0
last_right_key_time = 0

# Define the function to draw the grid
def draw_grid():
    for i in range(0, screen_width, grid_size):
        pygame.draw.line(screen, gray, (i, 0), (i, screen_height))
    for j in range(0, screen_height, grid_size):
        pygame.draw.line(screen, gray, (0, j), (screen_width, j))
    for obs in obstacles_list:
        add_obstacle(obs)
    grid = [[0 for j in range(screen_height // grid_size)] for i in range(screen_width // grid_size)]
    for obs in obstacles_list:
        grid[obs[0]][obs[1]] = 1
    return grid
def add_obstacle(pos):
    obstacle_rect = pygame.Rect(pos[0]*grid_size, pos[1]*grid_size, grid_size, grid_size)
    pygame.draw.rect(screen, (255, 165, 0), obstacle_rect)

prev_vehicle_pos = vehicle_pos.copy()
new_vehicle_pos = [0,0]
path = None
# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    prev_vehicle_pos = vehicle_pos
    start_node = Node(vehicle_pos)
    end_node = Node(target_pos)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                prev_vehicle_pos = vehicle_pos.copy()
                vehicle_pos[0] -= vehicle_speed
                if vehicle_pos in obstacles_list or vehicle_pos[0] < 0 or vehicle_pos[0] >= screen_width or vehicle_pos[1] < 0 or vehicle_pos[1] >= screen_height:
                    vehicle_pos = prev_vehicle_pos
                
                last_left_key_time = pygame.time.get_ticks()
            elif event.key == pygame.K_RIGHT:
                prev_vehicle_pos = vehicle_pos.copy()
                vehicle_pos[0] += vehicle_speed
                if vehicle_pos in obstacles_list or vehicle_pos[0] < 0 or vehicle_pos[0] >= screen_width or vehicle_pos[1] < 0 or vehicle_pos[1] >= screen_height:
                    vehicle_pos = prev_vehicle_pos
                last_right_key_time = pygame.time.get_ticks()

            elif event.key == pygame.K_UP:
                prev_vehicle_pos = vehicle_pos.copy()
                vehicle_pos[1] -= vehicle_speed
                if vehicle_pos in obstacles_list or vehicle_pos[0] < 0 or vehicle_pos[0] >= screen_width or vehicle_pos[1] < 0 or vehicle_pos[1] >= screen_height:
                    vehicle_pos = prev_vehicle_pos
                last_up_key_time = pygame.time.get_ticks()

            elif event.key == pygame.K_DOWN:
                prev_vehicle_pos = vehicle_pos.copy()
                vehicle_pos[1] += vehicle_speed
                if vehicle_pos in obstacles_list or vehicle_pos[0] < 0 or vehicle_pos[0] >= screen_width or vehicle_pos[1] < 0 or vehicle_pos[1] >= screen_height:
                    vehicle_pos = prev_vehicle_pos
                last_down_key_time = pygame.time.get_ticks()
            elif event.key == pygame.K_x:
                vehicle_pos = [0,0]
            elif event.key == pygame.K_c:
                path = path = astar(start_node, end_node, grid)

    # Clear the screen
    screen.fill(black)

    # Draw the grid
    grid = draw_grid()

    if path:
        for node in path:
            rect = pygame.Rect(node.position[0], node.position[1], node_size, node_size)
            pygame.draw.rect(screen, white, rect)
    # Draw the vehicle and target nodes
    vehicle_rect = pygame.Rect(vehicle_pos[0]*grid_size, vehicle_pos[1]*grid_size, grid_size, grid_size)
    pygame.draw.rect(screen, red, vehicle_rect)
    
    target_rect = pygame.Rect(target_pos[0]*grid_size, target_pos[1]*grid_size, grid_size, grid_size)
    pygame.draw.rect(screen, green, target_rect)

    
    

    # Update the screen
    pygame.display.flip()
    

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
