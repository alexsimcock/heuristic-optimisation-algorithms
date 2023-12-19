# Trialling different approaches to bit flipping
def bit_flip(x, index):
    return tuple([bit if bit_index != index else int(not(bit)) for bit_index, bit in enumerate(x)])

x = (1, 0, 1, 0, 1, 0, 1)
for index in range(len(x)):
    print(bit_flip(x, index))