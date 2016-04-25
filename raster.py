'''usage: python raster.py <spike_dir>'''

import sys
import glob
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    try:
        spike_dir = sys.argv[1]
    except IndexError:
        sys.exit(__doc__)

    min_time = float("inf")
    max_time = 0
    for i, spike_file in enumerate(glob.glob(spike_dir + "/*.spk")):
        print i, spike_file
        spike_times = np.fromfile(spike_file, dtype=np.int64)
        if spike_times[0] < min_time:
            min_time = spike_times[0]
        if spike_times[-1] > max_time:
            max_time = spike_times[-1]
        
        plt.vlines(spike_times, i + 0.5, i + 1.5, color='black')

    plt.axhline(color='black')
    plt.ylim(.5, len(glob.glob(spike_dir + "/*.spk")) + .5)
    plt.xlim(min_time, max_time)
    plt.title('White Noise')
    plt.xlabel('Time (microseconds)')
    plt.ylabel('Neuron #')
    
    plt.show()
