import pygame
from constants import *
from drone import Drone
import sys
map_grid = [
    [-1, -1, -1, 0, 0, -1, -1, -1],
    [-1, -1, -1, 0, 0, -1, -1, -1],
    [-1, -1, -1, 0, 0, -1, -1, -1],
    [ 0,  0,  0, 0, 0,  0,  0,  0],
    [ 0,  0,  0, 0, 0,  0,  0,  0],
    [-1, -1, -1, 0, 0, -1, -1, -1],
    [-1, -1, -1, 0, 0, -1, -1, -1],
    [-1, -1, -1, 0, 0, -1, -1, -1]
]


def main():
    
    global SCREEN, CLOCK
    
    pygame.init()
    
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    drone1 = Drone(300, 0)
    
    while True:


        drawRoad()
        drawGrid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        drone1.update()
        pygame.display.update()


def drawGrid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 2)

def drawRoad():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            color = BLUE if (blockPositiontoGridIndex(x, y, WINDOW_WIDTH, N) == 0) else GRAY
            pygame.draw.rect(SCREEN, color, rect, 0)

def blockPositiontoGridIndex(x, y, window_dim, N):
    scale_factor = N / window_dim
    i, j = ( int(x * scale_factor), int(y * scale_factor))
    return map_grid[i][j];

main()

