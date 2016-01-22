from copy import copy
import Trainer
import FFNN
import random


def target_function(inp):
    # return (2*inp)+3
    return  inp



tts = []
size = 200000
percept = FFNN.Perceptron(3)

for g in xrange(size):
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    answer = -1
    if y > target_function(x):
        answer = 1
    temp_trainer = Trainer.PTrainer(x,y,answer)
    tts.append(temp_trainer)


for t in tts:
    percept.train(t.trainer_inputs, t.trainer_answer)

print percept.weights


rights = filter(lambda x : percept.feedForward(x.trainer_inputs) == 1, tts)

right = 0
wrong = 0

for x in rights:
    if x.trainer_inputs[1] < target_function(x.trainer_inputs[0]):
        right = right + 1
    else:
        wrong = wrong + 1


import matplotlib.pyplot as plt


xs = map(lambda x : x.trainer_inputs[0],rights)
ys = map(lambda x : x.trainer_inputs[1],rights)

plt.scatter(xs,ys, marker = 'o')
plt.plot([-10,10],[-10,10])

plt.show()
plt.show()
print 'r:', right, 'w:', wrong