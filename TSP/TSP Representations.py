# My personal solution to representing the graph!
graph1 = {"Birmingham": {"Birmingham": 0,
                        "Oxford": 79,
                        "London": 126,
                        "Cambridge": 100,
                        "Newcastle": 206,
                        "York": 132},
         "Oxford":     {"Birmingham": 79,
                        "Oxford": 0,
                        "London": 60,
                        "Cambridge": 85,
                        "Newcastle": 267,
                        "York": 194},
         "London":     {"Birmingham": 126,
                        "Oxford": 60,
                        "London": 0,
                        "Cambridge": 64,
                        "Newcastle": 289,
                        "York": 215},
         "Cambridge":  {"Birmingham": 100,
                        "Oxford": 85,
                        "London": 64,
                        "Cambridge": 0,
                        "Newcastle": 229,
                        "York": 156},
         "Newcastle":  {"Birmingham": 206,
                        "Oxford": 267,
                        "London": 289,
                        "Cambridge": 229,
                        "Newcastle": 0,
                        "York": 85},
         "York":       {"Birmingham": 132,
                        "Oxford": 194,
                        "London": 215,
                        "Cambridge": 156,
                        "Newcastle": 85,
                        "York": 0}}

# Maybe a matrix representation would be more suitable?

def is_symmetric(graph):
    for node, neighbours in graph.items():
        for neighbour, dist in neighbours.items():
            if(graph[neighbour][node] != dist):
                return False
    return True

def is_equivalent(tour1, tour2):
    # Finds if tours are the same by manipulating second tour
    reverse_tour2 = tour2.copy()
    reverse_tour2.reverse()

    start_point = tour1[0]

    # First start tour2 from the same point as tour 1
    tour2_start_index = tour2.index(start_point)
    rtour2_start_index = reverse_tour2.index(start_point)

    tour2_modify = tour2[tour2_start_index:] + tour2[:tour2_start_index]
    rtour2_modify = reverse_tour2[rtour2_start_index:] + reverse_tour2[:rtour2_start_index]

    if (tour1 in (tour2_modify, rtour2_modify)):
        return True
    else:
        return False
    
def tour_cost(graph, tour):
    return 0

def greedy_nearest_neighbour(graph, start_point):
    # Assess all options, take shortest not already visited, until list is cleared
    unvisited = list(graph.keys())

    start_index = unvisited.index(start_point)
    visited = [unvisited.pop(start_index)]

    while len(unvisited) > 0:
        print("Visited:", visited)
        # visited[-1] equiv. to current node
        unvisited_neighbours = {key: val for key, val in graph[visited[-1]].items() if key not in visited}
        print("Unvisited neighbours", unvisited_neighbours)

        min_dist = min(unvisited_neighbours.values())
        min_dist_index = list(unvisited_neighbours.values()).index(min_dist)
        min_dist_key = list(unvisited_neighbours.keys())[min_dist_index]

        print("Visiting", min_dist_key)
        
        visited.append(unvisited.pop(unvisited.index(min_dist_key)))
    print("Final tour:", visited)
    return None

def exhaustive(graph):
    # start_point is arbitrary but reduces number of computations by a multiple of n
    nodes = list(graph.keys())
    start_node = nodes.pop(0)

    exhaustive_tours =  0

    return None

def create_symm_graph():
    nodes = ['A', 'B', 'C', 'D']

    arc = []
    for start_node in nodes:
        

        arcs = [start_node for start_node in graph]

        graph = {start_node: {end_node for end_node in nodes if end_node != start_node} for start_node in nodes}

    

    return graph



if __name__ == "__main__":
    print(create_symm_graph())

