import random
random.seed()
mylist = [ ( random.randint(0, 100), random.randint(0, 100) ) for k in range(10) ]
print(mylist)
