import utils
import collections
from collections import defaultdict
from collections import deque

class Solution(object):

    def leastStepQ1a(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque([(0, 0, 0)])
        # Visited set to avoid cycles
        visited = {(0, 0)}

        while queue:
            r, c, steps = queue.popleft()
            if r == m-1 and c == n-1:
                return steps

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < m and 
                    0 <= new_c < n and 
                    grid[new_r][new_c] == 0 and 
                    (new_r, new_c) not in visited
                ):
                    queue.append((new_r, new_c, steps + 1))
                    visited.add((new_r, new_c))
        return -1

        




if __name__ == '__main__':
    utils.A3_P1_1a_score()

