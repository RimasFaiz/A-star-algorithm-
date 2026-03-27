# A* Algorithm Implementation

A small interactive Python implementation of the A* (A-star) shortest-path search algorithm.

## Files
- `a_star_algorithm_implementation.py` — Interactive A* implementation (importable for testing).
- `tests/test_a_star.py` — Example pytest test for a simple graph.
- `README.md` — This file.

## Requirements
- Python 3.8+
- No external libraries required (uses the standard library `heapq`).
- For running tests: `pytest`.

## Overview
This script:
- Prompts the user to enter graph edges in the format `From To Cost` (e.g., `A B 1`).
- Treats edges as undirected by default (adds both directions to the adjacency list).
- Prompts the user to enter heuristic values for each node.
- Prompts for a start and goal node.
- Runs the A* algorithm and prints the optimal path and its total cost.

The implementation also exposes the `A_star(graph, heuristic, start, goal)` function so it can be imported and tested programmatically.

## Usage (interactive)
1. Run the script:
```bash
python a_star_algorithm_implementation.py
