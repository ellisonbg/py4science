import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2)

y = np.random.rand(10000)
x = np.random.randn(10000)

axes[0].hist(x, 100);
axes[1].hist(y, 100);
plt.show()
