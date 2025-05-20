import utils
import collections
from collections import defaultdict
import heapq

class Solution(object):

    def leastStepQ1a(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0]) # don't remove this line
        # Please code below
        print("m: ", m, " n: ", n)
        #queue = collections.deque(['A', 'B', 'C', 'D'])
        #print(queue.pop())

        if len(grid) == 1 and len(grid) == 1:
            return 0

        Record = {}

        #i: row   j: column
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

        def dfs_board(Record, startNode, endNode):
            frontier = collections.deque()
            visited_nodes = []
            path = []
            count = -1
            frontier.append(startNode)
            print("Initial frontier: ", list(frontier))
            #print(frontier)

            while frontier:
                currentNode = frontier.pop()

                if currentNode == endNode:
                    return count

                if not currentNode in visited_nodes:
                    print("Exploring: ", currentNode, "...")
                    visited_nodes.append(currentNode)
                    count += 1

                    if len(Record[currentNode]) == 0:
                        count = -1
                        return count

                    for node in Record[currentNode]:
                        print("Its child nodes: ", Record[currentNode])
                        frontier.append(node)
                        print("frontier: ", list(frontier))

        ans = dfs_board(Record, (0, 0), (m-1, n-1))
        return ans






if __name__ == '__main__':
    utils.A3_P1_1a_score()

