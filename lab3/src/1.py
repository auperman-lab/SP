import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 64
T = 1 / 128  # Sampling period
k = np.arange(N)
f = np.sin(2 * np.pi * 20 * k * T)  # Discrete signal

# Plot
plt.plot(k, f)
plt.grid(True)
plt.xlabel('Indecsul k', fontsize=16, fontname='Arial')
plt.ylabel('Y(t)', fontsize=16, fontname='Arial')
plt.title('Semnalul original', fontsize=16, fontname='Arial')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
