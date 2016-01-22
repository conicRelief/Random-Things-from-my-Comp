## This trains on three inputs. x,y, and a bias. A represents our desired answer.


class PTrainer:
    ## does each perceptron need its own trainer?
    def __init__(self,x,y,a):
        self.trainer_inputs = []
        self.trainer_inputs.append(x)
        self.trainer_inputs.append(y)
        self.trainer_inputs.append(1)
        self.trainer_answer = a