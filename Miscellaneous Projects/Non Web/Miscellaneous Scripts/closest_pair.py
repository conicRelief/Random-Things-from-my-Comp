# import random as rand
#
# list_of_random_number = []
# number_of_random_numbers = 10
# random_range = 10
# for x in range(number_of_random_numbers):
#     list_of_random_number.append((rand.randint(0,10),rand.randint(0,10),rand.randint(0,10)))
#
# print "\n".join([str (x) for x in list_of_random_number])
#
# import itertools as it
#
# print it.permutations()


t1 = (7,2,3)
t2 = (8,4,8)

import math
ans = math.sqrt((t1[0] - t2[0])**2 + (t1[1] - t2[1])**2 + (t1[2] - t2[2])**2 )
print ans