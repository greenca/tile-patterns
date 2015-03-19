import numpy as np
import matplotlib.pyplot as plt
import math
import itertools
import time

t = time.time()


numColours = 4
numRows = 3
numColumns = 3


def getRowCol(index):
    return (index/numColumns, index%numColumns)

def calcDist(x, y):
    x1, x2 = getRowCol(x)
    y1, y2 = getRowCol(y)
    return math.sqrt((y1-x1)**2 + (y2-x2)**2)

def calcCost(group):
    return min([calcDist(x, y) for x in group for y in group if y>x])


n = int(math.ceil(float(numRows*numColumns)/numColours))
cellVals = n*range(numColours)
cellVals = cellVals[:numRows*numColumns]

allGroupings = set()
for ordering in itertools.permutations(cellVals):
    curGroupings = []
    for i in range(numColours):
        curGroupings.append(frozenset([j for j in range(len(ordering)) if ordering[j]==i]))
    allGroupings.add(frozenset(curGroupings))

allGroupings = list(allGroupings)
allCosts = [min([calcCost(colourGroup) for colourGroup in groupings]) for groupings in allGroupings]

maxGroups = list([allGroupings[i] for i in range(len(allGroupings)) if allCosts[i]==max(allCosts)][0])

tiles = np.zeros((numRows, numColumns))

curVal = 0
for colour in maxGroups:
    for point in colour: 
        tiles[getRowCol(point)] = curVal
    curVal += 1

plt.imshow(tiles, interpolation='nearest')
plt.axis('off')
plt.show()

elapsed = time.time() - t
print elapsed
