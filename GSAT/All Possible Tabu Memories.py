# TODO make function sets importable from another file
functionset1 = {"f1": lambda x: not(x[0]) or not(x[1]) or not(x[2]),
                "f2": lambda x: (x[1]) or (x[2]),
                "f3": lambda x: (x[1]) or not(x[3]),
                "f4": lambda x: not(x[1]) or not(x[2]),
                "f5": lambda x: not(x[2]) or not(x[3]),
                "f6": lambda x: not(x[1]) or (x[3]),
                "f7": lambda x: (x[2]) or (x[3]),
                "f8": lambda x: (x[0]) or not(x[1]) or (x[2])}

functionset2 = {"f1": lambda x: (x[0]) or not(x[1]) or (x[2]),
                "f2": lambda x: not(x[3]) or (x[4]),
                "f3": lambda x: not(x[4]) or not(x[5]),
                "f4": lambda x: (x[6])}

functions = functionset2

# TODO add function docstrings

def eval(x):        
    return {func_name: int(function(x)) for func_name, function in functions.items()}

def unsolved_heuristic(x):
    return len(eval(x)) - sum(eval(x).values())

def flip_bit(x, index):
    return tuple([bit if bit_index != index else int(not(bit)) for bit_index, bit in enumerate(x)])
        
def get_neighbourhood(x, memory):
    """
    Return all possible bit flips with the resulting values, returned as a dictionary to help with retracing
    """
    flippable_bits = [i for i in range(len(memory)) if memory[i] == 0]
    return {index: flip_bit(x, index) for index in flippable_bits}

def get_minima(solution_dict, heuristic = unsolved_heuristic):
    """
    With a given heuristic returns ALL solutions that achieve the minimal (optimal) evaluation
    """
    best_eval = min([heuristic(solution) for solution in solution_dict.values()])
    return {flip_index: solution for flip_index, solution in solution_dict.items() if heuristic(solution) == best_eval}

class TabuNode():
    def __init__(self, x, memory, memory_length = 2):
        self.x = x
        self.memory = memory
        self.memory_length = memory_length
        
        self.h = unsolved_heuristic(x)
        self.children = dict()
        
    # Children are generated only when specified, after initialisation, to avoid accidental recursion
    def generate_children(self):
        def update_memory(flip_index):
            """Reduce all memory by one and set flipped bit memory to memory length"""
            updated_memory = [bit_memory - 1 if bit_memory > 0 else 0 for bit_memory in self.memory]
            updated_memory[flip_index] = self.memory_length
            return updated_memory
        
        children = get_minima(get_neighbourhood(self.x, self.memory), unsolved_heuristic)
        self.children = {index: TabuNode(child, update_memory(index), self.memory_length) for index, child in children.items()}
        
    def generate_next_tree_layer(self):
        # i.e. 'if dictionary is empty'
        if bool(self.children) is False:
            self.generate_children()
            return
        else:
            for child in self.children.values():
                child.generate_next_tree_layer()
                
    def generate_tree(self, depth):
        for layer_num in range(depth):
            self.generate_next_tree_layer()

if __name__ == "__main__":
    # Initialise values
    x = (0, 1, 0, 1, 0, 1, 0) #(0, 1, 0, 1)
    root_node = TabuNode(x, memory=[0] * len(x))
    root_node.generate_tree(depth = 3)
    
    def return_layer(root, final_layer = None, layer_number = 0):
        """Prints all nodes at a given layer, if not specified the deepest currently generated"""
        if (bool(root.children) is False or layer_number == final_layer):
            print(f"Value: {root.x}, Memory: {root.memory}")
            return
        else:
            for child in root.children.values():
                return_layer(child, final_layer, layer_number + 1)
    
    #https://simonhessner.de/python-3-recursively-print-structured-tree-including-hierarchy-markers-using-depth-first-search/
    def print_whole_tree(root, level = 0):
        print("  " * level, "-", root.x)
        for child in root.children.values():
            print_whole_tree(child, level + 1)

    print_whole_tree(root_node)
    #return_layer(root_node, 3)
    
    # We can now print out the entire search tree, the flips taken to get to any one element? all possible memory outcomes