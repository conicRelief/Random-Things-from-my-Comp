
test_cases = [
"2",
"Hello World",
"CodeEval",
"Quick Fox",
"A",
"San Francisco"
]



for test in sorted(test_cases[1:], key = len, reverse=True)[:int(test_cases[0])]:
    print test
import heapq

import sys
test_cases = open("inputs_and_stuff", 'r')


num = test_cases.readline()
print num
# for value in test_cases:
#         heappush(h, value)
# ...     return [heappop(h) for i in range(len(h))]
test_cases.close()


price_fluctuation = [-1,2,13,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
