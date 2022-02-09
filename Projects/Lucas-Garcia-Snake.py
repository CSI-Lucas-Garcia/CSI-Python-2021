from pickle import TRUE
import pygame
pygame.init()

blue = (93, 178, 255) #score
violet = (122, 78, 252) #food
brown = (219, 149, 86) #snake
green = (172, 254, 121) #background
red = (255, 25, 1) #game over

dis=pygame.display.set_mode((400,300))

pygame.display.set_caption("Snake game")
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=TRUE
    pygame.draw.rect(dis, brown,[200, 150, 10,10])
    pygame.display.update()

pygame.quit()
quit()