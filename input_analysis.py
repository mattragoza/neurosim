'''usage: python input_analysis.py <spikedata_path>'''

import sys
import glob
import math
import random
import numpy as np
from scipy import stats


def gen_exponential(lamb):
    return -(math.log((1-random.random()))/float(lamb))
    

if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        sys.exit(__doc__)

    n_bins = 15
    dof = n_bins - 2
    chi_crit = 22.362 #for this set of parameters
    
    print "Running Chi-Squared for Exponential at 95% significance..."
    print
    for i, spike_file in enumerate(glob.glob(path + "/*.spk")):
        print i, spike_file
        spike_times = np.fromfile(spike_file, dtype=np.int64)
        isi = np.diff(spike_times)  
        loc, scale = stats.expon.fit(isi, floc=0)
        lamb = 1/(np.mean(isi))
        n_samples = len(isi)
        rand_vals = []
        for j in range(n_samples):
            rand_vals.append(gen_exponential(lamb))
        bin_ranges = stats.expon.ppf(np.linspace(0, 1, n_bins + 1), loc=loc, scale=scale)
        hist, _ = np.histogram(rand_vals, bin_ranges)
        exp = np.ones(len(hist)) * n_samples/float(n_bins)
        chisq, p = stats.chisquare(hist, exp, ddof = dof)
    
        if chisq < chi_crit:
            print "PASSED"
        else:
            print "FAILED"