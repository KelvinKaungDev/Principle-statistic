import math
from statistics import variance
import numpy as np

score = [12.5, 18, 23, 28, 33, 38]
count = [3, 15, 23, 36, 17, 9]

def weighted_avg_and_std(score, count):
    average = np.average(score, weights=count)
    variance = np.average((score - average)**2, weights=count)
    return(average, math.sqrt(variance))

print(weighted_avg_and_std(score, count))


