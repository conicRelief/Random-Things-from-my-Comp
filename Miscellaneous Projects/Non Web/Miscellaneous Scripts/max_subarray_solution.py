# __author__ = 'otto'
# price_fluctuation = [13,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
#
# import math
# #
# # def A(i,j,list):
# #     left_sum = -math.inf()
# #     sum = 0
# #
# #     if i == j:
# #         return 0
# #     sum1 = A[i,math.floor(j/2)]
# #     sum2 = A[math.floor(j/2),j]
# #     maxSum = max([sum1,sum2])
# #     return maxSum
#
#
# """""
# Divide And Conquer
# 1) Divide
# 2) Conquer
# 3) Combine
#
# A[low,high]
#
# Divide in middle
#     A[low,mid]
#     A[mid,high]
#
# Conquer
#     Sum1 + MSum3(A,low,mid)
#     Sum2 = Sum3(A,mid + high)
# Combine
#     Max Sum = Max sum1,sum2 cross sum
#
# find max sum for subarray of form
#     A[1...mid], A[mid + 1...j] where low <=i j <high
#
#
# ===========
# PSUEDO CODE
# ===========
#
# FindMaxCrossSubarray(A, low, mid , high)
#     left-sum = -Inf
#     sum = 0
#     for i - mid downto low
#         sum = sum _ a[i]
#         if sum > left-sum then
#             left-sum - sum
#             max-left = i
#     right-sum = -inf
#     sum = 0
#     for j = mid +1 to high
#         su - sum + A[j]
#         if sum > right-sum then
#             right-sum = sum
#             max-rigth = j
#     return max max-left, max-right, left-sum + right sum
#
#
#
# """""
#
#
# # anneal.py
# # Use simulated annealing to find coefficients of a polynomial to match a generated training set
# #
# # This is a quick demo of how to do simulated annealing in Python.  Modify & use it as you wish.
# # Inspired from W.H. Press, S.A. Teukolsky, W.T. Vetterling & B.P. Flannery (1992), Numerical Recipes in C
# #
# # Oguz Yetkin 1/7/2009 oyetkin@gmail.com
#
# import math
# import random
# import pdb
#
# #degree of the polynomial +1.  This example solves the coefficients of a cubic polynomial, but can be easily modified to solve higher or lower order polynomials.
# n_coeffs = 4 #ax^3 + bx^2 + cx + d
#
# #length of our training set
# length = 10
#
# training_set = []
#
# #utility functions
# # def TESTfn(x):
#  # return math.pow(x,2)
#
# #This function will generate our training set (see the main function).  In real life, substitute your own data.
# def TESTfn(x):
#  #4x^3  - 2x^2 + 3x - 17,
#  #the coefficients we expect are [4,-2,3,-17]
#  return 4*x*x*x - 2*x*x + 3*x - 17
#
# #We are using this simple polynomial function as an example.  In real life, you can optimize anything *
# # * (I am not a mathematician)
# def poly(coeff_list,x):
#  ''' compute a polynomial with given coefficients and an x
#      For example, a coeff_list of [4,-2,3,-17] will compute 4x^3  - 2x^2 + 3x - 17
#  '''
#  count = 0
#  sum = 0
#  for coeff in reversed(coeff_list):
#   sum +=  math.pow(x, count) * coeff
#   count += 1
#  return sum
#
#
# def error(training_set, generated_set):
#  '''computes RMS error between to lists, assumes sets are the same size'''
#  sum = 0
#  for i in xrange(0,len(training_set)):
#   sum += math.pow((training_set[i] - generated_set[i]),2)
#  try:
#   return math.sqrt(sum)
#  except:
#   print "Exception happened, sum was: " + str(sum)
#   #return a large value so that the computation can continue.  The large error will cause the given sets to be discarded.
#   return 1000000
#
# def perturb(coeff_list, temperature):
#  '''perturb the coefficient list with the given temperature '''
#  for i in xrange(0, len(coeff_list)):
#   coeff_list[i] += (random.gauss(0,1)*temperature)
#  return coeff_list
#
# def anneal(inputs, training_set, coeff_list, expected_error):
#  temperature =  1.0
#  cooldown_factor = 0.995
#  #we initialize the best error to an arbitrary large value
#  best_error = 1000000
#
#  generated_set = []
#  best_coeff_list = coeff_list
#  current_error  = best_error
#
#  #print "steps,error,t,best_coeff_list,coeff_list,generated_set"
#  print " ------ training output below ------"
#  print
#
#  print "steps,improvements,e,t,[best_coeff_list],[coeff_list]"
#  improvements=0
#  steps = 0
#  while best_error > expected_error:
#   steps += 1
#   #generate new outputs
#   generated_set = []
#
#   for i in xrange(0,len(inputs)):
#    generated_set.append(poly(coeff_list, inputs[i]))
#   current_error = error(training_set,generated_set)
#
#   ##print everything
#   #print str(current_error)+","+str(temperature)+","+str(best_coeff_list)+","+str(coeff_list)+","+str(generated_set)
#
#   print str(steps)+","+str(improvements)+","+str(best_error)+","+str(temperature)+","+str(best_coeff_list)+","+str(coeff_list)
#   #print generated_set
#   #print training_set
#
#   if current_error < best_error:
#    #we found a better solution
#    improvements += 1
#    best_error = current_error
#    best_coeff_list = coeff_list[:]  #this is how you copy a list in Python
#    if temperature < 1.0:
#     temperature *= 2
#    #print " --- found better solution, increasing temperature --- "
#    # print "temperature="+str(temperature)
#    # print "best_error="+str(best_error)
#    # print "best_coeff_list="+str(best_coeff_list)
#    # print " training_set="+str(training_set)
#    # print "generated_set="+str(generated_set)
#   else:
#    #continue looking for a better solution
#    temperature *= cooldown_factor
#
#    coeff_list = best_coeff_list[:]
#
#
#    #print "temperature="+str(temperature)
#    #print temperature,
#    coeff_list = perturb(coeff_list, temperature)[:]
#    # print " --- still searching --- "
#    # print "temperature="+str(temperature)
#    # print "best_error="+str(best_error)
#    # print "best_coeff_list="+str(best_coeff_list)
#    # print " training_set="+str(training_set)
#    # print "generated_set="+str(generated_set)
#
#
#  print "best error was: " + str(best_error)
#  print " training set was: " + str(training_set)
#  print "generated_set was: " + str(generated_set)
#  return best_coeff_list[:]
#
#
#
#
#
# if __name__ == "__main__":
#  print "Simulated Annealing Demo in Python"
#  print "(c) Oguz Yetkin, 2009"
#  coeff_list = []
#  inputs = []
#  expected_error = 0.01
#
#  for i in xrange(0,n_coeffs):
#   #coeff_list.append(random.uniform(0,1))
#   coeff_list.append(0)
#
#  for i in xrange(int(-length/2),int(length/2)):
#   inputs.append(i)
#   training_set.append(TESTfn(i))
#
#  print coeff_list
#  print training_set
#
#  print "training now"
#
#  new_coeffs = anneal(inputs, training_set, coeff_list, expected_error)
#  print "new coefficients: "
#  print new_coeffs
#
# import random
#
# #
# # def random_a_la_variance( variance, bottom_range = 0, top_range = 0):
# #
# #
# # print random.mean([random.randint(0,10) for x in range(0,100)])
#
# ins = ["23\n","496\n"]
#
# for x in ins:
#     print reduce(lambda a, b: int(a) + int(b), filter(lambda s: s.isdigit() ,x))


#
# def closestPair(point):
#     xP = sorted(point, key = attrgetter('real'))

# class dynamical_system
word = "--AZza--00"

a = "a"
a = char(a)+1
print a
for x in word:
    if ord(x)<= ord('z') and ord(x)>= ord('A'):
        print x
