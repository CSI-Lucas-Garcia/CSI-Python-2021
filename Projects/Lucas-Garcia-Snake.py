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

x1 = 150
y1= 150

x1_change = 0 
y1_change = 0 

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=TRUE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    x1 += x1_change
    y1 += y1_change
    dis.fill(green)
    pygame.draw.rect(dis, brown,[x1, y1, 10,10])

    pygame.display.update()

    clock.tick(20)
pygame.quit()
quit()