from operator import attrgetter

def get_neighbourhood(x, memory):
    neighbourhood = []
    copy = x.copy()    
    flippable_bits = [i for i in range(len(memory)) if memory[i] == 0]

    neighbourhood = {index: tuple(copy[:index] + [int(not(copy[index]))] + copy[index + 1:]) for index in flippable_bits}
    return {flip_index: {"x": flipped_value, "f": eval(flipped_value), "h": sum(eval(flipped_value))} for flip_index, flipped_value in neighbourhood.items()}

class TabuNode():
    def __init__(self, x, memory):
        self.x = x
        self.f_values = eval(x)
        
        self.memory = memory
        
    def get_children(self):
        def get_child_memory(flip_index):
            # Reduce all memory by one and set flipped bit memory to 2
            updated_memory = [bit - 1 for bit in self.memory]
            updated_memory[flip_index] = 2
            return updated_memory
        
        flippable_indices = [i for i in range(len(self.memory)) if self.memory[i] == 0]
        flip_neighbours = {index: tuple(self.x[:index] + [int(not(self.x[index]))] + self.x[index + 1:]) for index in flippable_indices}
        self.children = {index: TabuNode(neighbour, get_child_memory(index)) for index, neighbour in flip_neighbours.items()}
        
    def print_node(self):
        print(f"X: {self.x}\nMemory: {self.memory}\nF-Value: {sum(self.f_values)}\nF: {self.f_values}")
        
        
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
    return len(eval(x)) - sum(eval(x))

if __name__ == "__main__":
    # Initialise values
    start_value = [0, 1, 0, 1]
    memory = [0] * len(start_value)
    
    start = TabuNode(start_value, memory)
    
    # Could be done through recursion? One parameter being max-recursion depth...
    step_counter = 0
    current_nodes = [start]
    while step_counter < 3:
        step_counter += 1
        
        # 1 Get neighbours who are not in memory
        for node in current_nodes:
            node.get_children()
            
            # 2 Generate their h value
            for flipped, child in node.children.items():
                print(f"Flipping {flipped} gives {child.x}, f-value: {sum(child.f_values)}")
            
            # 3 Find expandable nodes per node in current nodes...
            max_f = max([sum(child.f_values) for child in node.children])
            expandable_kids = [child for child in node.children if sum(child.f_values) == max_f]
            
            current_nodes.append(expandable_kids) ##
        
        #print(f"X: {start_value}\nMemory: {memory}")
        # 1
        #funcs = [("f" + str(i+1)) for i in range(len(functions))]
        #print("\n|Var|" + "|".join(funcs) + "|h-val|")
        #print("|-" * (len(start_value) + 6) + "|")
        #for flipped_bit, neighbour in get_neighbourhood(start_value, memory).items():
            # 2
        #    print("|" + "x" + str(flipped_bit + 1) + "|" + "|".join(map(str, map(int, neighbour["f"]))) + "|" + str(neighbour["h"]) + "|")