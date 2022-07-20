import numpy as np
import seaborn as sns
import warnings

x = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

warnings.simplefilter(action="ignore", category=FutureWarning);

sns.scatterplot(x, y);
sns.regplot(x, y);
