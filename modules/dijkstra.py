# This file is dijkstra.py

def _find_minimum(shortest_dist_param: dict, visited_list_param: list):
    min: str = list(shortest_dist_param)[0]
    for node in shortest_dist_param:
        if shortest_dist_param[node] == None: continue
        if node == min: continue
        if node in visited_list_param: continue
        if min in visited_list_param:
            min = node
        if shortest_dist_param[min] < shortest_dist_param[node]: continue
        min = node

    return min
    

def dijkstra_func(*args):
    if len(args) == 0: return None

    graph: dict = args[0]
    src: str = args[1]

    visited: list = []
    unvisited: list = ['A', 'B', 'C', 'D', 'E', 'F']

    shortest_dist: dict = {
        'A': None,
        'B': None,
        'C': None,
        'D': None,
        'E': None,
        'F': None,
    }

    prev_node: list = {
        'A': None,
        'B': None,
        'C': None,
        'D': None,
        'E': None,
        'F': None,
    }

    from_: str = src

    shortest_dist[from_] = 0
    sum: int = 0

    for node in graph[src]:
        shortest_dist[node] = graph[src][node]
        prev_node[node] = src
    
    if from_ in unvisited:
        visited.append(from_)
        unvisited.remove(from_)
    
    from_ = _find_minimum(shortest_dist_param = shortest_dist, visited_list_param = visited)

    for _ in unvisited[:]:
        for to_ in graph[from_]:
            sum = graph[from_][to_] + shortest_dist[from_]
            if shortest_dist[to_] == None or shortest_dist[to_] > sum:
                shortest_dist[to_] = sum
                prev_node[to_] = from_
            
            continue

        if from_ in unvisited:
            visited.append(from_)
            unvisited.remove(from_)

        from_ = _find_minimum(shortest_dist_param = shortest_dist, visited_list_param = visited)

    results: dict = {
        "dist": shortest_dist,
        "nodes": prev_node
    }

    return results


if __name__ == "__main__":
    dijkstra_func()