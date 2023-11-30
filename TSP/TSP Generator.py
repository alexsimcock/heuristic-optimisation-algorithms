import itertools
import random

#########################
#       GENERATORS      #
#########################

def generate_edges(nodes):
    bidirectional_edges = [(node1, node2) for node1 in nodes for node2 in nodes if node1 != node2]

    scanned_edges = []
    for edge in bidirectional_edges:
        if((edge[1], edge[0]) not in scanned_edges):
            scanned_edges.append(edge)

    return scanned_edges

def generate_consecutive_weights(edges):
    return {edge[1]: random.randint(1,5) for edge in list(enumerate(edges, start=1))}
    #return {edge[1]: edge[0] for edge in list(enumerate(edges, start=1))}

#############################
#       TOUR CHECKERS       #
#############################

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

def get_tour_cost(tour_edges, weight_func):
    tour_weight = [weight_func[edge] for edge in tour_edges]
    return sum(tour_weight)

def get_tour_edges(tour_nodes, graph_edges):
    # tour_nodes = ['A','B','C','D','A']
    tour_edges = []

    for i in range(0, len(tour_nodes)-1):
        edge = (tour_nodes[i], tour_nodes[i+1])
        reverse_edge = (tour_nodes[i+1], tour_nodes[i])

        if (edge in graph_edges):
            tour_edges.append(edge)
        elif (reverse_edge in graph_edges):
            tour_edges.append(reverse_edge)
        else:
            raise ValueError(f"Edge between {tour_nodes[i]} and {tour_nodes[i+1]} not found")
        
    return tour_edges

#################################

#################################

def generate_all_tours(nodes):
    # Start from the first given node every time, to reduce number needed
    all_permutations = [tuple(nodes[0]) + perm + tuple(nodes[0]) for perm in itertools.permutations(nodes[1:])]
    unique_permutations = []
    # Filter out reverse permutations
    for i in range(len(all_permutations)):
        reversed = all_permutations[i][::-1]
        r_new_start_index = reversed.index(nodes[0])
        r_same_start = tuple(nodes[0]) + reversed[r_new_start_index+1:] + reversed[:r_new_start_index]
        
        if (r_same_start not in all_permutations[:i]): # Cant just be reversed! Needs to start from A also.....
            unique_permutations.append(all_permutations[i])

    return unique_permutations

def exhaustive_search(graph):
    # Start point is arbitrary but will reduces number of computations by a multiple of n
    all_tours = generate_all_tours(graph['V'])

    results = {}
    for tour in all_tours:
        results[tour] = get_tour_cost(get_tour_edges(tour, graph['E']), graph['w'])

    return results

def greedy_nn_tour(graph, start_point):
    # Assess all options, take shortest not already visited, until list is cleared
    unvisited = graph['V']

    visited = [unvisited.pop(unvisited.index(start_point))]

    traversed_edges = []
    while len(unvisited) > 0:
        # visited[-1] equiv. to current node
        traversable_edges = [edge for edge in graph['E'] if (edge not in traversable_edges and visited[-1] in edge)]
        unvisited_neighbours = []

        min_dist = min(unvisited_neighbours.values())
        min_dist_index = list(unvisited_neighbours.values()).index(min_dist)
        min_dist_key = list(unvisited_neighbours.keys())[min_dist_index]
        
        visited.append(unvisited.pop(unvisited.index(min_dist_key)))
    return visited

if (__name__ == "__main__"):
    num_nodes = 4
    node_labels = ["ABCDEFG"[i] for i in range(0, num_nodes)]
    
    graph = {'V': node_labels, 'E': generate_edges(node_labels)}
    graph['w'] = generate_consecutive_weights(graph['E'])

    all_tour_costs = exhaustive_search(graph)
    optimum_cost = min(all_tour_costs.values())

    print(all_tour_costs)