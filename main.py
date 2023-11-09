import pygame
import constants as c
from init import *
from objects import *
from funcs import draw, action, check_collision, main_msg, lvl_msg, loader

lvl, angles, circle_to_win, c.fps = loader()

clock = pygame.time.Clock()
alive = True
animation = False
pause = False
while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
        if event.type == pygame.KEYDOWN and not pause:
            if event.key == pygame.K_SPACE and not animation:
                animation = True
    if not pause:
        if animation:
            c.M_Y-= c.M_S
        game_display.fill(c.BLACK)
        circles = draw(angles)
        mc = action(c.M_X,c.M_Y)
        if check_collision(c.M_X,c.M_Y, circles) and animation:
            pause = True
        else:
            if c.M_Y==c.Y+c.LENGTH and animation:
                animation = False
                angles = np.array(angles.tolist()+[90])
                c.M_Y = c.Y+c.LENGTH+c.M_DISTANCE
                circle_to_win-=1
                if circle_to_win==0:
                    with open("data/save.txt", "w") as f:
                        f.write(str(lvl+1))
                    lvl, angles, circle_to_win, c.fps = loader()
        main_msg(circle_to_win)
        lvl_msg(lvl)  
        angles-=1
    pygame.display.update()
    clock.tick(c.fps)
pygame.quit()

