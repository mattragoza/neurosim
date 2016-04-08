'''usage: python raster.py <spike_file>'''

import sys
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

	try:
		spike_file = sys.argv[1]
	except IndexError:
		sys.exit(__doc__)

	spike_times = np.fromfile(spike_file, dtype=np.int64)

	plt.vlines(spike_times, -0.1, 0.1, color='black')
	plt.axhline(color='black')
	plt.ylim(-1, 1)
	plt.xlim(spike_times[0], spike_times[-1])
	plt.show()
