from collections import deque
import pygame
from time import sleep, time
from constants import *
from drone import Drone
from utils import blockPositiontoGridIndex
from math import sin
import sys



def main():
    
    global SCREEN, CLOCK
    
    pygame.init()
    
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    play = False
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
                    xm, ym = blockPositiontoGridIndex(x, y, scale_factor)
                    if map_grid[xm][ym] > -1:
                        drone = Drone(xm, ym, f"Drone-{int(time()) % 100000}", RED)
                        drones.append(drone)
                    else:
                        print("DRONE CANNOT BE SPAWNED OUTSIDE THE CORRIDOR")
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    play = not play
                    print(play)

        if len(drones) > 0:
            for d in drones:
                d.render()
                if play:
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

