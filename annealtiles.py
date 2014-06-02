import numpy as np
import matplotlib.pyplot as plt
import math
import random


numColours = 4
numRows = 4
numColumns = 4
colours = range(numColours)

temp = 100000000
numSwaps = 10


def getRowCol(index):
    return (index/numColumns, index%numColumns)

def calcDist(x, y):
    x1, x2 = getRowCol(x)
    y1, y2 = getRowCol(y)
    return 1.0/((y1-x1)**2 + (y2-x2)**2)

def calcCost(cellVals):
    groups = [[i for i, c in enumerate(cellVals) if c==colour] for colour in colours]
    return np.mean([np.mean([calcDist(x, y) for x in group for y in group if y>x]) for group in groups])

def acceptProb(oldCost, newCost, curTemp):
    if newCost <= oldCost:
        return 1
    return math.exp((newCost - oldCost)/curTemp)



n = int(math.ceil(float(numRows*numColumns)/numColours))
cellVals = n*colours
cellVals = cellVals[:numRows*numColumns]
random.shuffle(cellVals)

curCost = calcCost(cellVals)

bestVals = cellVals
bestCost = curCost

while temp > 1:
    newVals = [v for v in cellVals]
    for i in range(numSwaps):
        i1 = random.choice(range(len(cellVals)))
        i2 = random.choice(range(len(cellVals)))
        newVals[i1], newVals[i2] = newVals[i2], newVals[i1]
    newCost = calcCost(newVals)

    if acceptProb(curCost, newCost, temp) > random.random():
        cellVals = newVals
        curCost = newCost

    if curCost < bestCost:
        bestCost = curCost
        bestVals = cellVals

    temp -= 1



tiles = np.zeros((numRows, numColumns))
for i, c in enumerate(bestVals):
    tiles[getRowCol(i)] = c

plt.imshow(tiles, interpolation='nearest')
plt.axis('off')
plt.show()
