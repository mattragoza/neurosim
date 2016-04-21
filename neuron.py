import numpy as np
import math


class Neuron:

    def __init__(self, base_rate, max_rate, rec_field, alpha=0.5, init_weights=None):

        self.base_rate = base_rate
        self.max_rate = max_rate
        self.firing_rate = base_rate
        self.alpha = alpha
        
        self.ouput  = [] #other neurons this neuron connects TO
        self.inputs = [] #neurons that connect to this neuron

        self.rec_field = rec_field
        if init_weights is None:
            self.weights = np.random.normal(0, 1, (rec_field, rec_field))
        elif init_weights.shape == (rec_field, rec_field):
            self.weights = init_weights
        else:
            raise ValueError("init_weights shape must match rec_field")

        self.spiked = False
            
    def update_firing_rate(self, stim):

        # take weighted sum of input stimulus
        input_sum = np.dot(self.weights.reshape(-1), stim.reshape(-1))

        # map the input sum into the firing rate range
        new_rate = sigmoid(input_sum, y_mid=self.base_rate, \
            y_range=2*(self.max_rate-self.base_rate))

        # update firing rate, taking into account the previous
        # rate weighted by the alpha parameter
        self.firing_rate = (1-self.alpha)*new_rate + self.alpha*self.firing_rate

        self.spiked = np.random.random() < self.firing_rate



def sigmoid(x, y_mid=0.5, y_range=1.0):
  return y_range*(1 / (1 + math.exp(-x)) - 0.5 + y_mid)


if __name__ == '__main__':

    rec_field = 3
    x = np.random.random((rec_field, rec_field)) #this is the input stimulus for now
    test_neuron = Neuron(70, 100, rec_field)
    for i in range(10):
        test_neuron.update_firing_rate(x)
    #     print test_neuron.firing_rate