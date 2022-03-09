from asyncore import loop
from pickle import TRUE
from turtle import update
import pygame
import random
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
snake_speed = 14
snake_block = 10
clock = pygame.time.Clock()

score_font = pygame.font.SysFont(None, 25)

def My_score(score):
    value = score_font.render("Your Score:" + str(score), True, violet)
    dis.blit(value, [0,0])

font_style = pygame.font.SysFont(None,25)

def my_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, brown, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/10, dis_height/2])

def gameloop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1= dis_height/2

    x1_change = 0 
    y1_change = 0 

    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10


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
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        pygame.draw.rect(dis, violet,[foodx, foody, snake_block,snake_block])
        # pygame.draw.rect(dis, brown,[x1, y1, snake_block,snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > (length_of_snake):
            del snake_List[0]
        
        for x in snake_List[: -1]:
            if x == snake_head:
                game_close == True

        my_snake(snake_block, snake_List)
        My_score(length_of_snake -1)

        pygame.display.update()


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            length_of_snake += 1

        clock.tick(snake_speed)

        


    pygame.quit()
    quit()

gameloop()



