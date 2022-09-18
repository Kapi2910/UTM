# have each drone check it's 8 neighbour hood
from collections import deque
import pygame
from time import sleep
from constants import *
from drone import Drone
from utils import blockPositiontoGridIndex
import sys



def main():
    
    global SCREEN, CLOCK
    
    pygame.init()
    
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    drones = deque()
    
    while True:

        sleep(0.5)
        drawRoad()
        drawGrid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    xm, ym =blockPositiontoGridIndex(x, y, scale_factor)
                    print(xm, ym)
                    drone = Drone(xm / scale_factor, ym / scale_factor)
                    drones.append(drone)
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if len(drones) > 0:
            for d in drones:
                d.update()
        
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
            x0, y0 = blockPositiontoGridIndex(x, y, scale_factor)
            color = BLUE if (map_grid[x0][y0] == 0) else PURPLE if (map_grid[x0][y0] == 1) else GRAY
            pygame.draw.rect(SCREEN, color, rect, 0)



main()

