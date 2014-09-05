tic()

using PyPlot

numColours = 4
numRows = 4
numColumns = 4
colours = 1:numColours

temp = 100000
numSwaps = 10

function getRowCol(index)
    return (div(index-1,numColumns)+1, (index-1)%numColumns+1)
end

function calcDist(x, y)
    x1, x2 = getRowCol(x)
    y1, y2 = getRowCol(y)
    return 1/((y1-x1)^2 + (y2-x2)^2)
end

function calcCost(cellVals)
    groups = [findin(cellVals, colour) for colour in colours]
    return mean([mean([calcDist(z[1], z[2]) for z in filter(a->a[1]<a[2], [(x,y) for x in group, y in group])]) for group in groups])
end

function acceptProb(oldCost, newCost, curTemp)
    if newCost <= oldCost
        return 1
    end
    return exp((newCost - oldCost)/curTemp)
end

n = iceil(numRows*numColumns/numColours)
cellVals = repmat(colours, n, 1)[1:numRows*numColumns]
shuffle!(cellVals)

curCost = calcCost(cellVals)

bestVals = cellVals
bestCost = curCost

while temp > 1
    newVals = copy(cellVals)
    for i=1:numSwaps
        i1 = rand(1:length(cellVals))
        i2 = rand(1:length(cellVals))
        newVals[i1], newVals[i2] = newVals[i2], newVals[i1]
    end
    newCost = calcCost(newVals)

    if acceptProb(curCost, newCost, temp) > rand()
        cellVals = newVals
        curCost = newCost
    end

    if curCost < bestCost
        bestCost = curCost
        bestVals = cellVals
    end

    temp -= 1
end

tiles = zeros(numRows, numColumns)
for i=1:length(bestVals)
    x,y = getRowCol(i)
    tiles[x,y] = bestVals[i]
end

imshow(tiles, interpolation="nearest")
axis("off")

toc()
