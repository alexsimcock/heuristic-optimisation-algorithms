from itertools import combinations

functions = {"f1": lambda x: not(x[0]) or not(x[1]) or not(x[2]),
             "f2": lambda x: (x[1]) or (x[2]),
             "f3": lambda x: (x[1]) or not(x[3]),
             "f4": lambda x: not(x[1]) or not(x[2]),
             "f5": lambda x: not(x[2]) or not(x[3]),
             "f6": lambda x: not(x[1]) or (x[3]),
             "f7": lambda x: (x[2]) or (x[3]),
             "f8": lambda x: (x[0]) or not(x[1]) or (x[2])}

#indices = [0, 1]
#x= [1,2].append([4,5])
#print(x)
#possible_indices = []
#for num_true in range(1, len(indices)-1):
#    print("m")#possible_indices.append(list(combinations(indices, r)))

x = [1, 0, 1, 0]
for f in functions.values():
    print(f(x))