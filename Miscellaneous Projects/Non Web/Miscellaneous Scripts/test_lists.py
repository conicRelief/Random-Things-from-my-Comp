list_a =  [10,11,13,14,15]
list_b =  map(lambda x: x+10, list_a)

mergedlist = zip(list_a, list_b)

print mergedlist

a_dict = {'test': None, 'another_test': None}

for x in a_dict:
    print "yo"