from operator import attrgetter

functions = {"f1": lambda x: not(x[0]) or not(x[1]) or not(x[2]),
             "f2": lambda x: (x[1]) or (x[2]),
             "f3": lambda x: (x[1]) or not(x[3]),
             "f4": lambda x: not(x[1]) or not(x[2]),
             "f5": lambda x: not(x[2]) or not(x[3]),
             "f6": lambda x: not(x[1]) or (x[3]),
             "f7": lambda x: (x[2]) or (x[3]),
             "f8": lambda x: (x[0]) or not(x[1]) or (x[2])}

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
        for index, child in children.items():
            print(f"flipping {index} gives child {child}")
        self.children = {index: TabuNode(child, update_memory(index), self.memory_length) for index, child in children.items()} 

if __name__ == "__main__":
    # Initialise values
    x = (0, 1, 0, 1)
    root_node = TabuNode(x, memory=[0] * len(x))
    current_nodes = [root_node]
    
    def generate_next_gen(root):
        # i.e. 'if dictionary is empty'
        if bool(root.children) is False:
            print("generating...")
            root.generate_children()
            return
        else:
            print(f"{root.x} has pre-existing children:")
            for child in root.children.values():
                print(f"running function for child of {root.x}, {child.x}")
                generate_next_gen(child)
    
    generate_next_gen(root_node)
    generate_next_gen(root_node)
    
    #children_list = [value for value in root_node.children.values()]

    # Problem with traversal resulting in incorrect printing of granchildren
    # A depth first search is ideal or breadth first?
    # I think to get all the nodes at one level (what we want) a breadth first will be ideal    