import random

columns = 50 #x
rows = 50 #y

#1: Genreate the Matrix
def makeLine(x):
    list = []
    for i in range (x):
        list.append(random.randint(0,1))
    return list

def startingImg(x,y):
    list = []
    matrix = []

    for i in range (y): 
        list = makeLine(x)
        matrix.append(list)
    return matrix

result = startingImg(columns,rows)


#2: Display the matrix as a tangable thing

import pygame

#initiate window
pygame.init()

cellsize = 10 #each cell is n x n pixels
screen = pygame.display.set_mode((columns*cellsize, rows*cellsize))
running = True


while running:
    # pygame.QUIT event means the user clicked X to close your window 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #draw matrix
    for col in range (columns): #x values
        for row in range (rows): #y values
            if result[row][col] == 1:
                color = (255, 255, 255, 255)
            else: 
                color = (0,0,0,0)
            pygame.draw.rect(screen, color, (col*cellsize, row*cellsize, cellsize, cellsize))
    
    #update screen
    pygame.display.flip()
