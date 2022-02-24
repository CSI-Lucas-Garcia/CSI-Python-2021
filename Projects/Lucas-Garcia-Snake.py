from asyncore import loop
from pickle import TRUE
from turtle import update
import pygame
import time 
pygame.init()

blue = (93, 178, 255) #score
violet = (122, 78, 252) #food
brown = (219, 149, 86) #snake
green = (172, 254, 121) #background
red = (255, 25, 1) #game over

#width and height of game

dis_width = 400
dis_height = 300

dis=pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption("Snake game")
game_over=False

# snake speed and how many blocks it equips
snake_speed = 18
snake_block = 10
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None,50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameloop():
    game_over = False
    game_clone = False

    x1 = dis_width/2
    y1= dis_height/2

    x1_change = 0 
    y1_change = 0 

#Play again
    while not game_over:
        while game_close == True:
            dis.fill(green)
            message("Game Over Press Q-Quit or P-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameloop()
        
    

#movement of snake
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=TRUE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block

    if x1>= dis_width or x1 < 0 or y1>= dis_height or y1 <0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(green)
    pygame.draw.rect(dis, brown,[x1, y1, snake_block,snake_block])

    pygame.display.update()

    clock.tick(snake_speed)


pygame.quit()
quit()