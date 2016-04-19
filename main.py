'''usage: python main.py <rec_field> <bar_width> <angle>'''
import sys
import neuron
import stimulus
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

if __name__ == '__main__':

	try:
		rec_field, width, deg, = map(int, sys.argv[1:])
	except:
		sys.exit(__doc__)

	rad = 2*np.pi * deg/360

	# init weights as an excitatory angled bar with an inhibitory border
	weights = 3*next(stimulus.rotating_bar(rec_field, 1, 0, width, rad)) \
		- 2*next(stimulus.rotating_bar(rec_field, 1, 0, 2*width, rad))

	n = neuron.Neuron(0, 100, rec_field, init_weights=weights)

	rate_x, rate_y = [], []
	t = 0

	for bar in stimulus.rotating_bar(rec_field, 360, 2*np.pi/360, width=width, norm=True):
		n.update_firing_rate(bar)
		rate_x.append(t)
		rate_y.append(n.firing_rate)
		t += 1

	plt.plot(rate_x, rate_y)
	plt.xlabel('Time, Stimulus angle')
	plt.ylabel('Firing rate')
	plt.xlim(0, 360)
	plt.ylim(-n.max_rate, n.max_rate)
	plt.show()
