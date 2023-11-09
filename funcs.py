import pygame
from init import *
import constants as c
from math import sin, cos, radians
import numpy as np

def draw(angles):
    circle = pygame.draw.circle(game_display, c.WHITE, (c.X,c.Y), c.R, 0)
    circles = []
    for i in range(len(angles)):
        _x = c.LENGTH*cos(radians(angles[i]))+c.X
        _y = c.LENGTH*sin(radians(angles[i]))+c.Y
        pygame.draw.line(game_display,
                                     c.WHITE,
                                     (c.X,c.Y),
                                     (_x,_y),
                                     7)
        circles.append(pygame.draw.circle(game_display, c.WHITE, (_x,_y), 10, 0))
    return circles


def action(x, y):
    return pygame.draw.circle(game_display, c.RED, (x, y),10,0)

def check_collision(x,y, circles):
    for circle in circles:
        for i in range(-5,5):
            if circle.collidepoint(x+i, y):
                return True
    return False

def main_msg(num):
    textMessage = str(num)
    font_and_size = pygame.font.Font("freesansbold.ttf",30)
    text_surface = font_and_size.render(textMessage,True,c.BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = ((c.X),(c.Y+5))
    game_display.blit(text_surface,text_rect)

def lvl_msg(num):
    textMessage = str(num)
    font_and_size = pygame.font.Font("freesansbold.ttf",30)
    text_surface = font_and_size.render(textMessage,True,c.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = ((50),(20))
    game_display.blit(text_surface,text_rect)
def loader():
    with open("data/save.txt", "r") as f:
        lvl = int(f.read())
    with open(f"data/lvl{lvl}.txt") as f:
        angles = [int(i) for i in f.readline().split(",")]
        circle_to_win = int(f.readline())
        fps = int(f.readline())
    return lvl, np.array(angles), circle_to_win, fps