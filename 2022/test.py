grid = ([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]])

m = len(grid)
n = len(grid[0])
Record = {}

for i in range(m):
    for j in range(n):

        currentNode = (i, j)
        print(currentNode)
        immedList = []
        originalList = []
                
        def findNeighbour(cn1, cn2, m, n):
            neigbourList = []
            if cn1+1 != m:
                neigbourList.append((cn1+1, cn2))

            if cn2+1 != n:
                neigbourList.append((cn1, cn2+1))

            if cn1-1 != -1:
                neigbourList.append((cn1-1, cn2))

            if cn2-1 != -1:
                neigbourList.append((cn1, cn2-1))

            return neigbourList
                
        originalList = findNeighbour(i, j, m, n)
        print("originalList: ", originalList)

        for k in range(len(originalList)):
            if grid[originalList[k][0]][originalList[k][1]] == 1:
                continue
            else:
                immedList.append(originalList[k])

        print("immedList: ", immedList)

        Record[currentNode] = immedList

print(Record)