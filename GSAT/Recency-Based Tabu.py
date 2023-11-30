# GSAT Algorithm for Problem Sheet 1
import itertools
import time

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

def get_neighbourhood(x):
    neighbourhood = []
    copy = x.copy()
    neighbourhood = [copy[:index] + [not(copy[index])] + copy[index + 1:] for index in range(0, len(start_value))]
    return {index: neighbour for index, neighbour in enumerate(neighbourhood)}

if __name__ == "__main__":
    #feasible_sol = list(itertools.product(range(0,2), repeat=4))
    # Initialise values
    start_value = [0, 1, 0, 1]
    print("Starting value:", start_value)
    cols = ["x_" + str(i + 1) for i in range(len(start_value))]
    
    memory = [0] * len(start_value)
    
    def available_memory():
        return [i for i in range(len(start_value)) if memory[i] == 0]
    
    print("Potential bits to flip:", available_memory())
    for bit_flip in available_memory():
        copy = start_value.copy()
        print("flipping index", bit_flip, ":", [copy[:bit_flip] + [int(not(copy[bit_flip]))] + copy[bit_flip + 1:]])

    # variables = ["x_" + str(k) for k in range(len(start_value))]
    # functions_str = ["F_" + str(k) for k in range(len(functions))]
    
    # print("| " + " | ".join(variables) + " |")
    # print("| --- "*len(start_value) + "|")
    # for neighbour in get_neighbourhood(start_value):
    #     print("| " + "  |  ".join(map(str, neighbour)) + " |")

    
    #print(solved_problems_heuristic(start_value))

    """
    results = {}
    for pot_sol in feasible_sol:
        results[pot_sol] = eval_sol(pot_sol, False)

    print("The following inputs are solutions:", [x for x, eval in results.items() if eval == 0])

    print("Using a GSAT approach with starting value:", start_value)

    current_val = start_value
    flips = 0
    tested_values = []

    # Stopping conditions for the GSAT: solution is found (eval == 0) or flips > max_flips
    while (eval_sol(current_val, False) != 0 and flips <= 4):
        print("Current value:", (current_val, eval_sol(current_val, False)))

        
        
        neighbourhood_eval = {neighbour: eval_sol(neighbour, False)
                            for neighbour in neighbourhood}#  if neighbour not in tested_values}
        neighbourhood_eval = sorted(neighbourhood_eval.items(), key = lambda x:x[1])
        
        print("Untested neighbourhood:", neighbourhood_eval)
        
        tested_values.append(current_val)

        flips += 1
        # Where current value not in already tested...?
        current_val = neighbourhood_eval[0][0]

        time.sleep(1)

    print("Final solution:", (current_val, eval_sol(current_val, False)))
    """