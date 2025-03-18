import numpy as np
import matplotlib.pyplot as plt

lower_limit = 0
upper_limit = 5
step = 0.001
size = int((upper_limit - lower_limit) / step) + 1

samples = np.random.rand(size) - 0.5  # Shift uniform distribution to [-0.5, 0.5]

t = np.linspace(lower_limit, upper_limit, size)  # Create time vector

plt.plot(t, samples)
plt.grid()
plt.title('Uniform Noise shifted to [-0.5, 0.5]')
plt.xlabel('Time (s)')
plt.ylabel('Noise Signal')
plt.show()
