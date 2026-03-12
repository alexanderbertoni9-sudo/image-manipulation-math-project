import random

#Hi this a test to see if tammy's compter can push code


rows = 100 #x | B/c you row row row your boat with your arms so rows are HORIZONTAL
columns = 100 #y | B/c columns stand stall so they are VERTICAL


#1: Genreate the Matrix

def makeMatrix(rows,cols):
    matrix = []
    
    for x in range(rows):
        line =[]
        for y in range(cols):
            line.append(random.uniform(0,255))
        matrix.append(line)
    
    return matrix

startingMatrix = makeMatrix(rows,columns)





#2: Display the matrix as a tangable thing

import pygame

#initiate window
pygame.init()

cellsize = 5 #each cell is n x n pixels
screen = pygame.display.set_mode((rows*cellsize, columns*cellsize))
running = True


while running:
    # pygame.QUIT event means the user clicked X to close your window 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #draw matrix
    for x in range (rows): #x values
        for y in range (columns): #y values
            rgb = startingMatrix[x][y]
            color = (rgb, rgb, rgb)
            pygame.draw.rect(screen, color, (x*cellsize, y*cellsize, cellsize, cellsize))
    
    #update screen
    pygame.display.flip()

#3: multiply the matrix by a kernal matrix

from numpy import array

edgeDetection = [
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
]

