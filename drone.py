import pygame
from time import sleep
from trigger import Trigger
from utils import polToCart, blockPositiontoGridIndex
from constants import *

class Drone:

    def __init__(self, x, y, name, color):
        self.x, self.y = (x, y)
        self.rect = pygame.Rect(x / scale_factor, y / scale_factor, BLOCK_SIZE, BLOCK_SIZE)
        self.id = name
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.color = color
        self.dx, self.dy = (0, 0)
        self.set_dir = False
        self.at_intersection = False

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.render()
        newpos = self.calcnewpos(self.rect)
        self.rect = newpos

    def intersection_trigger(self):
        Trigger.intersection()

    def calcnewpos(self,rect):
        posx, posy = blockPositiontoGridIndex(self.rect.topleft[0], self.rect.topleft[1], scale_factor)
        if not self.set_dir:
            if posy == half_length-1 or posy == half_length:
                self.dx = BLOCK_SIZE if posx - half_length <= 0 else -BLOCK_SIZE
            if posx == half_length-1 or posx == half_length:
                self.dy = BLOCK_SIZE if posy - half_length <= 0 else -BLOCK_SIZE
            self.set_dir = True
        
        if posx < 0 or posx > N:
            self.dx = 0
        if posy < 0 or posy > N:
            self.dy = 0
        
        if posy == half_length-1 or posy == half_length and posx == half_length-1 or posx == half_length:
            self.at_intersection = True
            # self.intersection_trigger()
        else:
            self.at_intersection = False
        return rect.move(self.dx, self.dy)

    

    # Find a modular way to to check a n-neighborhood of a cell
    def neighbors(self):
        pass

    