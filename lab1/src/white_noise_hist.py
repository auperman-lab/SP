import numpy as np
import matplotlib.pyplot as plt

lower_limit = 0
upper_limit = 5
step = 0.001
t = np.arange(lower_limit, upper_limit, step)

samples = np.random.rand(len(t)) -0.5

plt.hist(samples, bins=20, edgecolor='black', alpha=0.7, density=True)
plt.grid()
plt.title('Histogram of Uniform Noise [-0.5, 0.5]')
plt.xlabel('Time (s)')
plt.ylabel('Frequency Density')
plt.show()