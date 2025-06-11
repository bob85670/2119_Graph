import utils
from collections import defaultdict, deque
class Solution(object):
    def leastNumBus(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """

        if source == target:
            return 0;

        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        if source not in stop_to_routes or target not in stop_to_routes:
            return -1

        # Model as 
        # Node: bus route 
        # Edge: pairs of routes that share at least 1 bus stop
        graph = defaultdict(list);
        for stop, route_list in stop_to_routes.items():
            for i in range(len(route_list)):
                for j in range(i + 1, len(route_list)):
                    r1, r2 = route_list[i], route_list[j]
                    graph[r1].append(r2)
                    graph[r2].append(r1)

        # BFS
        queue = deque([(route, 1) for route in stop_to_routes[source]]) # (route, count)
        visited = set()
        while (queue):
            curr_route, trip = queue.popleft()
            if curr_route in visited:
                continue
            visited.add(curr_route)

            if target in routes[curr_route]:
                return trip

            for next_route in graph[curr_route]:
                if next_route not in visited:
                    queue.append((next_route, trip + 1))
        return -1
        
    


if __name__ == '__main__':
    utils.score()

