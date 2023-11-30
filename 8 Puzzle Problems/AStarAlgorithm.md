Let OPEN be the list of generated, but not yet examined nodes.
1. Start with OPEN containing the initial state.
2. Do until a goal state is found or no nodes are left in OPEN:
    a. Take the best node (lowest f value) in OPEN and generate its successors.
    b. For each successor do:
        i. if it has not been generated before, evaluate it and add it to OPEN.
        ii. otherwise change the parent, if this path is better and modify accordingly the costs for the depending nodes.

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
