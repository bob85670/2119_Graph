import utils_p2
from collections import defaultdict
import heapq
class Solution(object):
    def theLeastPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = float("inf");
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 5) for _ in range(n)] # k + 5 is a safety buffer to avoid index out-of-bounds errors
        for u, v, cst in flights: # build graph
            adj[u].append([v, cst])

        dist[src][0] = 0
        minHeap = [(0, src, -1)] # cost, node, stops
        while len(minHeap):
            cst, node, stops = heapq.heappop(minHeap)
            if dst == node:
                return cst
            if stops == k or dist[node][stops + 1] < cst: # pruning
                continue
            for nei, w in adj[node]:
                nextCst = cst + w
                nextStops = stops + 1
                if dist[nei][nextStops + 1] > nextCst:
                    dist[nei][nextStops + 1] = nextCst
                    heapq.heappush(minHeap, (nextCst, nei, nextStops))

        return -1



if __name__ == '__main__':
    utils_p2.score()

