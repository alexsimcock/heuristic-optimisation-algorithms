def f1(x):
    return not(x[0]) or not(x[1]) or not(x[2])
    
def f2(x):
    return (x[1]) or (x[2])

def f3(x):
    return (x[1]) or not(x[3])

def f4(x):
    return not(x[1]) or not(x[2])
    
def f5(x):
    return not(x[2]) or not(x[3])
    
def f6(x):
    return not(x[1]) or (x[3])

def f7(x):
    return (x[2]) or (x[3])
    
def f8(x):
    return (x[0]) or not(x[1]) or (x[2])
    
functions = [f1, f2, f3, f4, f5, f6, f7, f8]

def f(x):        
    return [function(x) for function in functions]

def solved_problems_heuristic(x):
    return sum(f(x))

def get_neighbourhood(x, memory):
    neighbourhood = []
    copy = x.copy()
    flippable_bits = [i for i in range(len(memory)) if memory[i] == 0]
    
    neighbourhood = {index: tuple(copy[:index] + [int(not(copy[index]))] + copy[index + 1:]) for index in flippable_bits}
    return {flip_index: {"x": flipped_value, "h": solved_problems_heuristic(flipped_value)} for flip_index, flipped_value in neighbourhood.items()}

if __name__ == "__main__":
    # Initialise values
    start_value = [0, 1, 0, 1]
    memory = [0] * len(start_value)
    
    # 1 Get neighbours who are not in memory
    # 2 Generate their manhattan value
        # Generate a dictionary with neighbours and manhattan value, for the purpose of output it would be nice to include f values
    # 3 Choose best available. repeat
    print(f"X: {start_value}\nMemory: {memory}")    
    # 1
    for flipped_bit, neighbour in get_neighbourhood(start_value, memory).items():
        # 2
        full_dict = {flipped_bit: {"value": neighbour, "f": f(neighbour), "h": solved_problems_heuristic(neighbour)}}
        print(f"flipping bit {flipped_bit} gives: {neighbour}, heuristic value {solved_problems_heuristic(neighbour)}")
        
    

    # variables = ["x_" + str(k) for k in range(len(start_value))]
    # functions_str = ["F_" + str(k) for k in range(len(functions))]
    
    # print("| " + " | ".join(variables) + " |")
    # print("| --- "*len(start_value) + "|")
    # for neighbour in get_neighbourhood(start_value):
    #     print("| " + "  |  ".join(map(str, neighbour)) + " |")

    
    #print(solved_problems_heuristic(start_value))