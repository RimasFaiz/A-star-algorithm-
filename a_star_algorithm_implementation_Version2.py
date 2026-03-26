# -*- coding: utf-8 -*-
"""A Star Algorithm Implementation

Interactive script refactored so functions can be imported for testing.
"""

import heapq

def Get_Graph_Input():
    graph = {}
    print("enter edges for example:A B 1(From To Cost).write DONE when youre finished:")
    while True:
        edge = input('Edge:').strip()
        if edge.lower() == 'done':
            break
        try:
            From_Node, To_node, Cost_str = edge.split()
            cost_value = float(Cost_str)
            if From_Node not in graph:
                graph[From_Node] = []
            if To_node not in graph:
                graph[To_node] = []
            graph[From_Node].append((To_node, cost_value))
            graph[To_node].append((From_Node, cost_value))

            print(f"  Added: {From_Node} <-> {To_node} (cost: {cost_value})")
        except ValueError:
            print(" ERROR Invalid. Cost must be a number, and input must have 3 parts.")
        except:
            print(" ERROR Invalid input format.")
    return graph

def Get_Heuristics(graph_data):
    heuristic = {}
    nodes = sorted(graph_data.keys())
    print(f"\nEnter heuristic for each node:")
    for node in nodes:
        while True:
            try:
                h = float(input(f"h({node}) = "))
                heuristic[node] = h
                break
            except ValueError:
                print("  Error: Enter a valid number")
    return heuristic

def A_star(graph_data, heuristic_data, start_node, goal_node):
    # priority queue that stores (f_cost, g_cost, node)
    queue = [(0, 0, start_node)]
    came_from = {}
    g_cost = {start_node: 0} # Actual cost from start to current node

    while queue:
        # Get the node with the lowest f(n)_cost
        current_f, current_g, current = heapq.heappop(queue)

        # Skip if we found a better path before
        if current in g_cost and current_g > g_cost[current]:
            continue
        if current == goal_node:
            # Recreate path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start_node)
            path.reverse()
            return path, g_cost[goal_node]

        for neighbor, edge_cost in graph_data.get(current, []):
            new_g_cost = current_g + edge_cost
            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                h_cost = heuristic_data.get(neighbor, 0)
                f_cost = new_g_cost + h_cost
                heapq.heappush(queue, (f_cost, new_g_cost, neighbor))
                came_from[neighbor] = current
    return None, 999999

def run_interactive():
    main_graph = Get_Graph_Input()
    main_heuristic = Get_Heuristics(main_graph)

    start_node = input("\nStart node: ").strip()
    goal_node = input("Goal node: ").strip()

    path, cost = A_star(main_graph, main_heuristic, start_node, goal_node)
    if path:
        print(f"\nThe Optimal Path is: {' → '.join(path)}")
        print(f"The Total Cost: {cost}")
    else:
        print("\nNo path has been found!")

if __name__ == "__main__":
    run_interactive()