import random


def recursive_add(base, size):
    if size == 1:
        return sum(base)
    else:
        tempM = []
        for y in range(size):
            tempM.append(base[y] + base[y+1])
        return recursive_add(tempM, size -1)

base_size = 11

randomBase = [random.randrange(0,2) for x in range(base_size)]

import itertools

print [x for x in itertools.permutations([], 1)]
print randomBase
print  recursive_add(randomBase, len(randomBase)-1)