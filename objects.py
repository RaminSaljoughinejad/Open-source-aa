import pygame
import constants as c
from init import *
from math import sin, cos, radians
import numpy as np

circle = pygame.draw.circle(game_display, c.WHITE, (c.X,c.Y), c.R, 0)

lines = []
lines.append(pygame.draw.line(game_display,
                                     c.WHITE,
                                     (c.X,c.Y),
                                     (c.LENGTH*cos(radians(0))+c.X,c.LENGTH*sin(radians(0))+c.Y),
                                     7))
angles = np.array([0,45,90,135,180,225,270,315,360])

mc = pygame.draw.circle(game_display, c.RED, (c.M_X, c.M_Y),10,0)