import pygame
from random import randint
from copy import deepcopy

size = (700, 700) 
FPS = 25
width = height = 20
n = size[1] // width

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

next_status = [[0 for i in range(n)] for i in range(n)]
current_status = [[randint(0,1) for i in range(n)] for i in range(n)]


def check_cell(current_status, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_status[j][i] == 1:
                count +=1

    if current_status[y][x] == 1:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

count = 1
cycle= []

running = True
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()    
        
    for i in range(n):
        pygame.draw.line(screen, pygame.Color('white'), (0, (i+1)*width), (700, (i+1)*width))
        pygame.draw.line(screen, pygame.Color('white'), ((i+1)*height, 0), ((i+1)*width, 700))

    for x in range(1, n - 1):
        for y in range(1, n - 1):
            if current_status[y][x] == 1:
                pygame.draw.rect(screen, pygame.Color('pink'), (x*height+2, y*height+2, height-2, height-2))
            next_status[y][x] = check_cell(current_status, x, y)   

    
    current_status = deepcopy(next_status)
    
    if (count%2) == 0:
        if current_status == cycle:
            print("GAME OVER")
            running = False

    if (count%2) == 0:
        cycle = current_status
    count += 1
    
    pygame.display.flip()
    clock.tick(FPS)

input('Press ENTER to exit')