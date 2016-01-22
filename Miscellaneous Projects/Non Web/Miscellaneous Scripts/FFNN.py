


import random


class Perceptron:
    c = 0.1 # This is our learning rate/velocity
    def __init__(self, size):
        if size > 0:
            self.weights = self.generateRandomList(size)
        else:
            print "\n \n A perceptron needs to include at least one weight. You've created a perceptron with 0 inputs, 0 weights..."
            raise
    def dotProduct(self, vec1, vec2):
        return sum(map(lambda x: x[0]*x[1], zip(vec1,vec2)))
    # Generate list of random numbers between -1, and 1. Precision describes
    def generateRandomList(self, size, precision = 3):
        t_list = [random.randrange(-1*(10**precision),1*(10**precision)) for _ in range(0, size)]
        return  map(lambda x: float(x)/float(10**precision), t_list)


    def activate(self,sum):
        if sum > 0:
            return 1
        else:
            return -1
    def feedForward(self, inputz):
        if len(inputz) == len(self.weights):
            return self.activate(self.dotProduct(inputz,self.weights))
        else:
            print "\n \n input and weights lenghts mismatch. Fix that please."
            raise
    def train(self,input,desired):
      #  print input, desired
        guess = self.feedForward(input)
        # print guess
        # print self.weights
        error = desired - guess
        # print error
        # print error
        self.weights = map(lambda x: x - float(self.c*error*x), self.weights)
        # print self.weights , self.c
        # print "====="
a = Perceptron(5)

