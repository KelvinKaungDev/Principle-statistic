import numpy as np

from scipy.stats import norm

mean = 5.46
stdev = np.sqrt(2.5)

n = 100;	confidence = 0.95

z_crit = np.abs(norm.ppf((1 - confidence) / 2))
print("This is for 95 percent")
print((mean - stdev*z_crit / np.sqrt(n), mean + stdev*z_crit / np.sqrt(n)))

