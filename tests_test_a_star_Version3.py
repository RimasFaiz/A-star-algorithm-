from a_star_algorithm_implementation import A_star

def test_simple_graph():
    # construct a small undirected graph
    graph = {
        'A': [('B', 1.0), ('C', 4.0)],
        'B': [('A', 1.0), ('C', 2.0)],
        'C': [('A', 4.0), ('B', 2.0)],
    }
    heuristic = {'A': 2.0, 'B': 1.0, 'C': 0.0}
    path, cost = A_star(graph, heuristic, 'A', 'C')
    assert path == ['A', 'B', 'C']
    assert cost == 3.0