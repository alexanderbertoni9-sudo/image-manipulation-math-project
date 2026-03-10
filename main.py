import random

columns = 3 #x
rows = 3 #y

# Genreate the Matrix
def makeLine(x):
    list = []
    for i in range (x):
        list.append(random.randint(0,1))
    return list
def startingImg(x,y):
    list = []
    matrix = []

    for i in range (x):
        list = makeLine(x)
        for j in range (y):
            matrix.append(list)

    return matrix

result = startingImg(columns,rows)
print(result)
