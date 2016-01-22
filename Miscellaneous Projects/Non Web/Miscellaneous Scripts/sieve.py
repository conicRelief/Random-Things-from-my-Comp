# class mini_sieve:
#     def __init__(self, hash = None):
#         if hash is not None:
#             pass # Then set the sieve up
#         else:
#             pass # initiate a seive using sieve hash.
#     def pump(self,a_function,n, range = None, training_file_url = None ):
#         # This function will add a function to our sieve. The sieves job will be to pick
#         # the best function based on run-time for input of a set size. The rationale being that
#         # some functions, like a polinomial time function for example, operate faster on a smaller input domain.
#         # There exists c,d el R and i,j el R such that cn + d > in^2 + j
#         # This algorithm learns to find input
#
#         pass
#
#     def seivify(self):
#         pass



import statistics

items = [2/21, 3/19, 2/16, 3/14,2/11,6,7,8,9]
items2 = [2, 3, 4,5,6,7,8,9,10,11]

import random as rd

def random_unique_sorted_list(other_list = []):
    i1 = []
    for x in xrange(10):
        num = rd.randint(0,100)
        if num not in i1 and num not in other_list:
            i1.append(num)
    return sorted(i1)


l1 = random_unique_sorted_list()
l2 = random_unique_sorted_list(l1)
print l1,l2

print sorted( l1 + l2)

def slice_per(source, step):
    return [source[i::step] for i in range(step)]

def slice_per2(source,step):
    print [source[i::step]]
print slice_per(l1,4)
# def split_list(a_list):
#     half = len(a_list)/2
#     return a_list[:half], a_list[half:]
#
#
# print split_list(items)

print statistics.median([1,2])
