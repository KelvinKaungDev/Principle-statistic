import numpy as np
import seaborn as sns
import warnings


x = np.array([3.6, 2.0, 3.4, 2.8, 2.9, 3.3, 4.1, 2.5, 3.2, 3.5])

y = np.array([23, 11, 20, 17, 15, 21, 24, 13, 19, 25])

r = np.corrcoef(x, y)

print(r)

import scipy.stats

r1 = scipy.stats.pearsonr(x, y)

print(r1)

warnings.simplefilter(action="ignore", category=FutureWarning);
sns.scatterplot(x, y);
sns.regplot(x, y);

