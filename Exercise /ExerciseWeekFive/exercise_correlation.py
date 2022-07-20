import numpy as np

x = np.array([3.26, 2.6, 3.35, 2.86, 3.82, 2.21, 3.47])

y = np.array([33.8, 29.8, 33.5, 30.4, 36.4, 27, 35])

r = np.corrcoef(x, y)

print(r)

import scipy.stats

r1 = scipy.stats.pearsonr(x, y)

print(r1)
