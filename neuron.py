import numpy as np
import math

class Neuron:
    def __init__(self, base_rate, max_rate, rec_field, alpha=0.5, init_weights=None):
        self.base_rate = base_rate
        self.firing_rate = base_rate
        self.ouput = [] #other neurons this neuron connects TO
        self.inputs = [] #neurons that connect to this neuron
        self.alpha = alpha
        self.max_rate = max_rate
        #TODO: make check that init_weights is same dimension as rec_field
        self.weights = init_weights
        if init_weights is None:
            self.weights = np.random.random((rec_field, rec_field))
            
    def update_firing_rate(self, stim):

        res = np.dot(np.reshape(self.weights, -1), np.reshape(stim, -1))
        new_rate = sigmoid(res)*(self.max_rate - self.base_rate) + self.base_rate
        weighted_rate = (1-self.alpha)*new_rate + self.alpha*(self.firing_rate) #prob not best way to do this

        self.firing_rate = weighted_rate #no sigmoid yet
        print('fr: ', self.firing_rate)
#         if updated_rate >= 0:
#             self.firing_rate = updated_rate
#         else:
#             self.firing_rate = 0

def sigmoid(x):
  return 2*(1 / (1 + math.exp(-x)) - 0.5)



rec_field = 3
x = np.random.random((rec_field, rec_field)) #this is the input stimulus for now

if __name__ == '__main__':
    test_neuron = Neuron(70, 100, rec_field)
    for i in range(10):
        test_neuron.update_firing_rate(x)
    #     print test_neuron.firing_rate