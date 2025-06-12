# 2119_Graph
This is an assignment testing knowledge of graph data structures.

# Graph Data Structures Overview

- **Dijkstra’s Algorithm**  
  Specialized for weighted graphs.  
  Uses a priority queue to optimize for shortest paths.  
  Limited to non-negative weights and cannot detect negative cycles.

- **Breadth-First Search (BFS)**  
  Ideal for unweighted graphs.  
  Uses a queue for level-order exploration.

- **Depth-First Search (DFS)**  
  Suited for general exploration, especially unweighted graphs. 
  Uses a stack for deep traversal.  
  Not optimized for shortest paths.

- **Bellman-Ford Algorithm**  
  Slower but handles negative weights.  
  Can detect negative cycles, making it more versatile for specific applications.