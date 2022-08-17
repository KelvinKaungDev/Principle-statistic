# Assume you are draw a number 1 to 10 for 50 times. Calculate mean, median and mode. Draw a boxplot of data.​

from statistics import median
import numpy as np
import random
import matplotlib.pyplot as plt

randomlist = [];

for i in range(0.50) :
    n = random.randint(1,10)
    randomlist.append(n)

plt.boxplot[randomlist]
plt.show()

import numpy as np
from scipy import stats
mean   = np.mean(randomlist)
median = np.median(randomlist)
mode   = stats.mode(randomlist)

print(mean)
print(median)
print(mode)

