'''usage: python main.py'''
import sys
import neuron
import stimulus
import numpy as np
import matplotlib.pyplot as plt

np.random.seed()

if __name__ == '__main__':
	
	dt = 1e-3 # ms
	total_t = 360

	stim_size, bar_width = 15, 3
	stim = stimulus.rotating_bar(stim_size, total_t, 2*np.pi/total_t,
		width=bar_width)

	base_rate = 218 * dt # Hz
	max_rate  = 351 * dt # Hz
	min_rate  = base_rate - (max_rate-base_rate)

	stim_shape = (stim_size, stim_size)

	input_layer = []
	for i in range(3):
		for j in range(3):
			center = (2+5*j,2+5*i)
			n = neuron.Neuron(base_rate, max_rate, stim_shape)
			n.weights = 3*stimulus.circle(stim_size, 2, True, center) \
					    - stimulus.circle(stim_size, 4, True, center)
			input_layer.append(n)

	nout = neuron.Neuron(base_rate, max_rate, (9,))
	nout.set_inputs(input_layer)
	nout.weights = np.array([ 0,-99,  0,
							 99,  0, 99,
							  0,-99,  0])

	nxx = nout
	print(nxx.weights)

	x, y, spike_times = [], [], []
	for t, s in enumerate(stim):

		for n in nout.inputs:
			n.update_firing_rate(s)
		nout.update_firing_rate()

		y.append(nxx.firing_rate)
		if nxx.spiked:
			spike_times.append(t)

		x.append(t)

	plt.plot(x, y, color=(0.9,0.9,0.9))
	plt.vlines(spike_times, base_rate+0.25*(max_rate-base_rate),
		                    base_rate-0.25*(max_rate-base_rate))
	plt.xlabel('Time (ms)')
	plt.ylabel('Firing rate')
	plt.xlim(0, total_t)
	plt.ylim(min_rate, max_rate)
	plt.show()
