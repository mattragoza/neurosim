import neuron
import stimulus
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

if __name__ == '__main__':

	n = neuron.Neuron(base_rate=10, max_rate=20, rec_field=100)
	n.weights = next(stimulus.rotating_bar(n.rec_field, 1, 0, angle=0, width=10, norm=False))

	rate_x, rate_y = [], []
	t = 0

	for i in range(20):
		n.update_firing_rate(stimulus.zeros(n.rec_field))
		rate_x.append(t)
		rate_y.append(n.firing_rate)
		t += 1

	for bar in stimulus.rotating_bar(n.rec_field, 60, 2*np.pi/60, width=10, norm=True):
		n.update_firing_rate(bar)
		rate_x.append(t)
		rate_y.append(n.firing_rate)
		t += 1

	for i in range(20):
		n.update_firing_rate(stimulus.zeros(n.rec_field))
		rate_x.append(t)
		rate_y.append(n.firing_rate)
		t += 1

	plt.plot(rate_x, rate_y)
	plt.ylim(n.base_rate-5, n.max_rate+5)
	plt.show()
