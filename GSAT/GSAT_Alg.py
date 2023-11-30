# GSAT Algorithm for Problem Sheet 1
import itertools
import time

def f_1(x):
    return x[0] or x[1] or x[2]

def f_2(x):
    return not(x[0]) or x[1] or x[2]

def f_3(x):
    return not(x[1]) or x[2]

def f_4(x):
    return not(x[1]) or x[3]

def f_5(x):
    return x[1] or not(x[2])

def f_6(x):
    return not(x[2]) or x[3]

def f_7(x):
    return x[1] or not(x[3])

def f_8(x):
    return x[2] or not(x[3])

def f(x):
    return [f_1(x), f_2(x), f_3(x), f_4(x), f_5(x), f_6(x), f_7(x), f_8(x)]

def eval_sol(x, print_f):
    result = f(x)
    if(print_f):
        print(result)
    return result.count(False)

feasible_sol = list(itertools.product(range(0,2), repeat=4))
start_value = (0, 0, 0, 0)

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

    neighbourhood = [tuple(current_val[:index])
                    + tuple([not(current_val[index])])
                    + tuple(current_val[index + 1:])
                    for index in range(0, len(start_value))]
    
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