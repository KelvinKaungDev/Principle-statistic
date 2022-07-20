import numpy as np
import scipy.stats as stats

x = np.array([252, 244, 241, 234, 230, 223])
y = np.array([2, 2.2, 2.4, 2.6, 2.8, 3])

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(slope)
print(intercept)
print(r)

result = intercept + (slope * x);
print("The linear model is", result);
