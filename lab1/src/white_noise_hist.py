import numpy as np
import matplotlib.pyplot as plt

lower_limit = 0
upper_limit = 5
step = 0.01
size = int((upper_limit-lower_limit)/(step))+1
print(size)
samples = np.random.rand(size) -0.5

plt.hist(samples, bins=20, edgecolor='black', alpha=0.7, density=True)
plt.grid()
plt.title('Histogram of Uniform Noise [-0.5, 0.5]')
plt.xlabel('Time (s)')
plt.ylabel('Frequency Density')
plt.show()