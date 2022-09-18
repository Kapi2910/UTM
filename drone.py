import pygame
from time import sleep
from utils import polToCart
from constants import *

class Drone():

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.vector = (x, y)

    def render(self):
        pygame.draw.rect(self.screen, RED, self.rect)

    def update(self):
        self.render()
        newpos = self.calcnewpos(self.rect)
        print(self.rect.topleft)
        sleep(0.5)
        self.rect = newpos

    def calcnewpos(self,rect):
        dy, dx = (BLOCK_SIZE, 0)

        curr_x, curr_y = (self.rect.topright)
        
        if curr_x > WINDOW_WIDTH - BLOCK_SIZE or curr_x < 0:
            dx = 0

        if dy > WINDOW_HEIGHT  - BLOCK_SIZE or curr_y < 0:
            dy = 0

        return rect.move(dx,dy)

    