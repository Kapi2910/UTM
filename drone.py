import pygame
from time import sleep
from utils import polToCart, blockPositiontoGridIndex
from constants import *

class Drone():

    def __init__(self, x, y, name, color):
        self.rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        self.name = name
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.color = color
        print(self.color)
        self.posx, self.posy = (x, y)
        self.dx, self.dy = (0, 0)
        self.set_dir = False

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.render()
        newpos = self.calcnewpos(self.rect)
        self.rect = newpos


    def calcnewpos(self,rect):
        if not self.set_dir:
            half_length = N // 2
            self.posx, self.posy = blockPositiontoGridIndex(self.rect.topleft[0], self.rect.topleft[1], scale_factor)
            print(self.posx, self.posy)
            if self.posy == 5 or self.posy == 6:
                self.dx = BLOCK_SIZE if self.posx - half_length <= 0 else -BLOCK_SIZE
            if self.posx == 5 or self.posx == 6:
                self.dy = BLOCK_SIZE if self.posy - half_length <= 0 else -BLOCK_SIZE
            self.set_dir = True
        
        if self.posx < 0 or self.posx > N:
            self.dx = 0
        if self.posy < 0 or self.posy > N:
            self.dy = 0
        

        return rect.move(self.dx, self.dy)

    