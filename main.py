import random

#Hi this a test to see if tammy's compter can push code


rows = 4 #x | B/c you row row row your boat with your arms so rows are HORIZONTAL
columns = 4 #y | B/c columns stand stall so they are VERTICAL


#1: Genreate the Matrix

def makeMatrix(rows,cols):
    matrix = []
    
    for x in range(rows):
        line =[]
        for y in range(cols):
            line.append(random.randint(0,255))
        matrix.append(line)
    print(matrix)
    return matrix

startingMatrix = makeMatrix(rows,columns)

#3: multiply the matrix by a kernal matrix

import numpy as np

edgeDetection = [
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
]
"""
def applyKernal(matrix,kernal,row,col):
    matrixForExport = []
    for x in range (row):
        line =[]
        for y in range(col):

editedMatrix = applyKernal(startingMatrix, edgeDetection,rows,columns)
print(editedMatrix)

"""
# These two functions were created by help with ChatGPT, based off a rough build I had. After the orginal
# faberication by the GPT, I then append to them to include all parts of the matrix (middle and bottom rows)

def safe_get(matrix, x, y):
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[x]): # ISSUE: This checks if area wanted to be grab 
        # is out of the range of the matrix, if it is just return center values which is a BIG PROBLEM. 
        # THIS NEEDS TO BE FIXED TO check if there is no bottom, then check if there is no left/ride side 
        # to take from, THEN check and take from center (that line should only run 4 times per any quadilaterals)
        return matrix[x][y]
    else:
        return 0


def getBaseMatrix(matrix, x, y):
    top_left = safe_get(matrix, x-1, y-1)
    top_middle = safe_get(matrix, x-1, y)
    top_right = safe_get(matrix, x-1, y+1)

    middle_left = safe_get(matrix, x, y-1)
    middle_middle = safe_get(matrix, x, y)
    middle_right = safe_get(matrix, x, y+1)

    bottom_left = safe_get(matrix, x+1, y-1)
    bottom_middle = safe_get(matrix, x+1, y)
    bottom_right = safe_get(matrix, x+1, y+1)

    baseMatrix = [
        [top_left, top_middle, top_right],
        [middle_left, middle_middle, middle_right],
        [bottom_left, bottom_middle, bottom_right]
    ]

    return baseMatrix


matrixWindow = getBaseMatrix(startingMatrix, 0, 0)
print(matrixWindow)

#Display matrix nicely in terminal 

def prettyPrint(matrix,msg):
    print(msg)
    for x in range (len(matrix)):
        print("[", end= " ")
        for y in range (len(matrix[x])):
            print(matrix[x][y], end=" ")
        print("]")
        print("\n")


if rows * columns <= 64: #Prints the matrix if the total items is less than 64 (realistacly a 6x6 matrix)
    prettyPrint(startingMatrix,"Starting Matrix: ")
    prettyPrint(matrixWindow,"Window Matrix; center (0,0)")


#2: Display the matrix as a tangable thing

import pygame

#initiate window
pygame.init()

cellsize = 100 #each cell is n x n pixels
screen = pygame.display.set_mode((rows*cellsize, columns*cellsize))
running = True


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw matrix
    for x in range(rows):
        for y in range(columns):
            rgb = startingMatrix[x][y]
            color = (rgb, rgb, rgb)
            pygame.draw.rect(screen, color, (x*cellsize, y*cellsize, cellsize, cellsize))

    #update screen
    pygame.display.flip()