import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 64
T = 1 / 128  # Sampling period
k = np.arange(N)
f = np.sin(2 * np.pi * 108 * k * T)  # Original discrete signal

# Fourier Transform
F = np.fft.fft(f)

# Plot magnitude of FFT
plt.plot(k, np.abs(F))
plt.grid(True)
plt.xlabel('k (indice în domeniul frecvenţei)', fontsize=16, fontname='Arial')
plt.ylabel('|F(k)|', fontsize=16, fontname='Arial')
plt.title('Modulul transformatei Fourier', fontsize=16, fontname='Arial')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
