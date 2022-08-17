import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 12
p = 0.167
x = np.arange(0, n + 1)

ans_one = binom.pmf(5, n, p)
print(ans_one)

binomial_pmf = binom.pmf(x, n, p)

plt.plot(x, binomial_pmf, color = 'blue')
plt.title(f"Binomial distribution, (n = {m}, p = {p})")

binomial_cdf = binom.cdf(x, n, p)

plt.plot(x, binomial_pmf, color = 'red')
plt.title(f"Binomial distribution, (n = {m}, p = {p})")
plt.show();
