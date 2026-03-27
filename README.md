# A* Algorithm Implementation

Interactive Python implementation of the A* (A‑star) shortest-path search algorithm for undirected weighted graphs.

## Overview
- Reads an undirected weighted graph from standard input.
- Reads a heuristic value for each node.
- Runs A* from a specified start node to a specified goal node.
- Prints the found optimal path and its total cost, or reports that no path exists.

## Files
- `a_star_algorithm_implementation.py` — the script containing the interactive interface and the `A_star` function.
- `tests/test_a_star.py` — example pytest unit test (if present in the repository).

## Requirements
- Python 3.8 or newer
- Uses only Python standard library (`heapq`)
- For tests: `pytest` (optional)

## Input format (interactive)
1. Enter edges one per line in the format:
   FromNode ToNode Cost
   Example:
   ```
   A B 1
   B C 2
   A C 4
   DONE
   ```
   Enter `DONE` to finish entering edges.
   - Edges are treated as undirected: each input edge adds both directions with the same cost.

2. Enter heuristic values for each node when prompted:
   ```
   h(A) = 2
   h(B) = 1
   h(C) = 0
   ```

3. Enter start and goal nodes:
   ```
   Start node: A
   Goal node: C
   ```

## Example session
Input:
```
Edge: A B 1
Edge: B C 2
Edge: A C 4
Edge: DONE

Enter heuristic for each node:
h(A) = 2
h(B) = 1
h(C) = 0

Start node: A
Goal node: C
```

Output:
```
The Optimal Path is: A → B → C
The Total Cost: 3.0
```

## Public function (importable)
Signature:
```python
A_star(graph_data, heuristic_data, start_node, goal_node)
```
- graph_data: dict mapping node -> list of (neighbor, cost) tuples
- heuristic_data: dict mapping node -> heuristic value (float)
- start_node, goal_node: node identifiers (strings)
- Returns: (path, cost)
  - path: list of node identifiers from start to goal, or None if no path found
  - cost: numeric total cost of the returned path (or 999999 if no path found)

Usage example:
```python
from a_star_algorithm_implementation import A_star

graph = {
    'A': [('B', 1.0), ('C', 4.0)],
    'B': [('A', 1.0), ('C', 2.0)],
    'C': [('A', 4.0), ('B', 2.0)],
}
heuristic = {'A': 2.0, 'B': 1.0, 'C': 0.0}
path, cost = A_star(graph, heuristic, 'A', 'C')
```

## Implementation notes
- Uses a priority queue (`heapq`) storing tuples `(f_cost, g_cost, node)` where `f_cost = g_cost + h(node)`.
- Tracks best-known `g_cost` values and a `came_from` map to reconstruct the path.
- If a heuristic value is missing for a node, the code uses a default of `0` for that node.
- If the goal is unreachable, the function returns `(None, 999999)`.

## Complexity
- Time complexity: O(E log V) in typical implementations using a binary heap (E = edges, V = vertices).
- Space complexity: O(V + E) for graph storage and bookkeeping.

## Testing
Run available tests with:
```bash
pytest -q
```
