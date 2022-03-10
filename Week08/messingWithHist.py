# learning hist

import numpy as np
import matplotlib.pyplot as plt

normData = np.random.normal(size = 1000)

plt.hist(normData)
plt.show()