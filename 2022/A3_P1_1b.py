import utils
import collections
from collections import defaultdict
from collections import deque


class Solution(object):
    def leastStepQ1b(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0]) # don't remove this line
        # Please code below
        if grid[0][0] == 1:
            grid[0][0] = 0
            eliminate_used = 1
        else:
            eliminate_used = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque([(0, 0, 0, eliminate_used)]) # (row, col, steps, walls_eliminated)
        visited = {(0, 0, eliminate_used)}

        while queue:
            r, c, steps, walls = queue.popleft()
            if r == m-1 and c == n-1:
                return steps

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n:
                    if grid[new_r][new_c] == 0 and (new_r, new_c, walls) not in visited:
                        queue.append((new_r, new_c, steps + 1, walls))
                        visited.add((new_r, new_c, walls))
                    elif grid[new_r][new_c] == 1 and walls == 0 and (new_r, new_c, 1) not in visited:
                        queue.append((new_r, new_c, steps + 1, 1))
                        visited.add((new_r, new_c, 1))


        return -1
        

if __name__ == '__main__':
    utils.A3_P1_1b_score()

