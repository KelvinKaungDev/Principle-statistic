import math
from statistics import variance
import numpy as np

data = [25, 30, 35, 40, 45, 50]
body_weights = [8, 4, 3, 4, 5, 6]

def weighted_avg_and_std(data, body_weights):
    average = np.average(data, weights=body_weights)
    variance = np.average((data - average)**2, weights=body_weights)
    return(average, math.sqrt(variance))

print(weighted_avg_and_std(data, body_weights))


