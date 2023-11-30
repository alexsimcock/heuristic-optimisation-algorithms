import numpy as np

def get_tile_coords(puzzle):    
    tile_coords = {}
    for row_index, row in enumerate(puzzle):
        for col_index, tile in enumerate(row):
            tile_coords[tile] = (row_index, col_index)
    return tile_coords

def get_neighbours(puzzle):
    def swap_tiles(puzzle, coords1, coords2):
        swapped_puzzle = puzzle.copy()
        
        value1 = swapped_puzzle[coords1]
        value2 = swapped_puzzle[coords2]
        
        swapped_puzzle[coords1] = value2
        swapped_puzzle[coords2] = value1
        
        return swapped_puzzle
    
    tile_coords = get_tile_coords(puzzle)
    empty_x, empty_y = tile_coords[0]
    
    # How can I expand on this to +-1 all dimensionsssss.....
    empty_adj_coords = [(empty_x + 1, empty_y), (empty_x - 1, empty_y), (empty_x, empty_y + 1), (empty_x, empty_y - 1)]
    empty_adj_coords = [coords for coords in empty_adj_coords if coords in tile_coords.values()]
    
    return [swap_tiles(puzzle, adj_coords, (empty_x, empty_y)) for adj_coords in empty_adj_coords]

if __name__ == "__main__":
    current = np.array([[0, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    print(current)
    print(get_neighbours(current))