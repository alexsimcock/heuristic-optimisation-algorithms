import numpy as np
from operator import attrgetter

# todo: refactor for consistency

def puzzle_to_ascii(puzzle):
    """Prints tile permutation in an ASCII grid
    Args:
        tile_permutation (list): 2-dimensional list containing tile labels
    Returns:
        str
    Raises:
        ValueError - when permutation is not given as a 2d list
    """
    
    if(np.array(puzzle).ndim != 2):
        raise ValueError("Permutation is non-2 dimensional")
    
    return "\n".join(" | ".join([str(tile) for tile in row]) for row in puzzle)

def get_tile_coords(puzzle):
    """Generates a dictionary {tile: (x_coord, y_coord)}
    Args:
        tile_permutation (list): 2-dimensional list containing tile labels
    Returns:
        dict
    """
    
    tile_coords = {}
    for row_index, row in enumerate(puzzle):
        for col_index, tile in enumerate(row):
            tile_coords[tile] = (row_index, col_index)
    return tile_coords

def get_neighbours(puzzle):
    """Generates a list of permutations that are one tile shift away
    Args:
        tile_permutation (list): 2-dimensional list containing tile labels
    Returns:
        list
    """
    
    def swap_tiles(puzzle, coords1, coords2):
        swapped_puzzle = puzzle.copy()
        
        value1 = swapped_puzzle[coords1]
        value2 = swapped_puzzle[coords2]
        
        swapped_puzzle[coords1] = value2
        swapped_puzzle[coords2] = value1
        
        return swapped_puzzle

    # def swap_tiles(puzzle, coords1, coords2):
    #     swapped_puzzle = puzzle.copy()
    #     swapped_puzzle[coords1[0]][coords1[1]], swapped_puzzle[coords2[0]][coords2[1]] = swapped_puzzle[coords2[0]][coords2[1]], swapped_puzzle[coords1[0]][coords1[1]]
    #     return swapped_puzzle
    
    tile_coords = get_tile_coords(puzzle)
    empty_x, empty_y = tile_coords[0]
    
    # How can I expand on this to +-1 all dimensionsssss.....
    empty_adj_coords = [(empty_x + 1, empty_y), (empty_x - 1, empty_y), (empty_x, empty_y + 1), (empty_x, empty_y - 1)]
    empty_adj_coords = [coords for coords in empty_adj_coords if coords in tile_coords.values()]
    
    return [swap_tiles(puzzle, adj_coords, (empty_x, empty_y)) for adj_coords in empty_adj_coords]

def manhattan_heuristic(current, goal):
    """Finds and sums manhattan distances of each tile
    Args:
        current (list): 2-dimensional list containing tile labels
        goal (list): 2-dimensional list containing tile labels
    Returns:
        int
    """
    
    current_indices = get_tile_coords(current)
    goal_indices = get_tile_coords(goal)
    
    if(current_indices.keys() != goal_indices.keys()):
        raise KeyError("Tiles in goal and current nodes are not equivalent") # maybe should be value error as type is correct but just not quite right
    
    tile_distances = {}
    
    # If changing token for empty tile - adjust this code
    non_empty_tiles = (tile for tile in current_indices.keys() if tile != 0)
    
    for tile in non_empty_tiles:
        current_coord = current_indices[tile]
        goal_coord = goal_indices[tile]
        tile_distances[tile] = abs(current_coord[0] - goal_coord[0]) + abs(current_coord[1] - goal_coord[1])
        
    return sum(tile_distances.values())

class PuzzleNode():
    def __init__(self, puzzle, goal, parent, g):
        self.puzzle = puzzle
        self.goal = goal
        
        self.parent = parent
        self.children = [] # Will this cause problems?
        
        self.g = g
        self.h = manhattan_heuristic(puzzle, goal)
        self.f = self.g + self.h
        
    def change_parent(self, new_parent):
        self.parent = new_parent
        # h value is unchanged so only g needs to be recalculated
        self.g = new_parent.g + 1
        self.f = self.h + self.g

if __name__ == "__main__":
    goal =  np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    current = np.array([[0, 8, 7], [6, 5, 4], [3, 2, 1]])

    # Start with open containing the initial state.
    search_root = PuzzleNode(current, goal, parent=None, g=0)
    
    open_nodes = [search_root]
    closed_nodes = []
    generated_nodes = set([search_root])
    
    # Do until a goal state is found or no nodes are left in OPEN:
    counter = 0
    while len(open_nodes) > 0 and counter < 10:
        
        # Take best node in open (by lowest f) and generate its successors
        # It would be nice to switch this method to prefer to continue down current tree, current way is not very human
        # Done! using reversed
        best_node = min(reversed(open_nodes), key = attrgetter('f'))
        
        print("-----------------------------------------------")
        print("Expanding best node:")
        print(best_node.puzzle)
        
        # CHECK FOR GOAL == CURRENT
        if np.array_equal(best_node.puzzle, goal):
            print("goal found!")
            break
        
        successor_nodes = [PuzzleNode(puzzle, goal, parent=best_node, g = best_node.g + 1)
                           for puzzle in get_neighbours(best_node.puzzle) if not np.array_equal(puzzle, search_root.puzzle)]
        
        open_nodes.remove(best_node)
        closed_nodes.append(best_node)
    
        # For each successor do:
        for successor in successor_nodes:
            print("\nCurrent successor")
            print(successor.puzzle)
            print(f"f value: {successor.f} = {successor.h} (h) + {successor.g} (g)")
            # i. if it has not been generated before, evaluate it and add it to OPEN.
            if (successor not in generated_nodes):
                print("successor not generated before")
                # condition not picking up on nodes generated
                successor.parent = best_node
                best_node.children.append(successor)
                open_nodes.append(successor)
            # ii. otherwise change the parent, if this path is better and modify accordingly the costs for the depending nodes
            # Successor h value will not change! So we only need to check g value...
            elif (best_node.g < successor.parent.g):
                print("successor previously generated but updating with lower f")
                successor.parent.children.remove(successor)
                successor.parent = best_node
                successor.re_eval()
                best_node.children.append(successor)
            else:
                print("sucessor previously generated with a lower f")
        
        # Adds successors into the generated nodes set to be checked later
        generated_nodes.update(successor_nodes)
        
        counter += 1
        
    # #traversal_tree
    # print("\n\nTraversal Tree")
    
    # visited = [] # List to keep track of visited nodes.
    # queue = []     #Initialize a queue
    
    # visited.append(search_root)
    # queue.append(search_root)

    # while queue:
    #     s = queue.pop(0) 
    #     print (s.puzzle)
    #     print(f"f ({s.f}) = h ({s.h}) + g ({s.g})")

    #     for child in s.children:
    #         if child not in visited:
    #             visited.append(child)
    #             queue.append(child)