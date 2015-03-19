tic()

using PyPlot

numColours = 4
numRows = 4
numColumns = 2

function getRowCol(index)
    return (div(index-1,numColumns)+1, (index-1)%numColumns+1)
end

function calcDist(x, y)
    x1, x2 = getRowCol(x)
    y1, y2 = getRowCol(y)
    return sqrt((y1-x1)^2 + (y2-x2)^2)
end

function calcCost(group)
    return minimum([calcDist(z[1], z[2]) for z in filter(a->a[1]<a[2], [(x,y) for x in group, y in group])])
end

n = iceil(numRows*numColumns/numColours)
cellVals = repmat(1:numColours, n, 1)
cellVals = cellVals[1:numRows*numColumns]

allGroupings = Set()
for ordering in permutations(cellVals)
    curGroupings = Array{Int,1}[]
    for i in 1:numColours
        push!(curGroupings, filter(j->ordering[j]==i, 1:length(ordering)))
    end
    push!(allGroupings, curGroupings)
end

allGroupings = collect(allGroupings)

allCosts = [minimum([calcCost(colourGroup) for colourGroup in groupings]) for groupings in allGroupings]

maxGroups = allGroupings[indmax(allCosts)]

tiles = zeros(Int, numRows, numColumns)

curVal = 0
for colour in maxGroups
    for point in colour
        x,y = getRowCol(point)
        tiles[x,y] = curVal
    end
    curVal += 1
end

imshow(tiles, interpolation="nearest")
axis("off")

toc()
