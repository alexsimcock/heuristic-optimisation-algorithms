# TODO define a generic SAT node

def eval(x, functions):
    return {func_name: function(x) for func_name, function in functions.items()}

class SatNode():
    def __init__(self, x, eval_func):
        self.x = x
        self.eval_func = eval_func
        self.children = dict()
        
    def unsolved_heuristic(self):
        return len(self.eval_func) - sum([function(self.x) for function in self.eval_func])

    def printx(self):
        print(f"X: {self.x} | Heuristic Evaluation: {self.unsolved_heuristic()} | Function Values: {[int(function(self.x)) for function in self.eval_func]}")
        return
    
    def get_all_neighbours():
        return
    
if __name__ == "__main__":
    functionset2 = [lambda x: (x[0]) or not(x[1]) or (x[2]),
                    lambda x: not(x[3]) or (x[4]),
                    lambda x: not(x[4]) or not(x[5]),
                    lambda x: (x[6])]
    
    x = SatNode((0, 1, 0, 1, 0, 1, 0), functionset2)
    x.printx()

# TODO define an inherited GSAT, TABU and A* node