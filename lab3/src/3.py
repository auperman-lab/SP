import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 64
T = 1 / 128  # Sampling period
k = np.arange(N)
f = np.sin(2 * np.pi * 20 * k * T)  # Example: 20 Hz sine wave

# Fourier Transform
F = np.fft.fft(f)
magF = np.abs(F)

# Frequency axis in Hz
hertz = k * (1 / (N * T))  # This gives freq = k * 2 Hz

# Plot only the first half of the spectrum
plt.plot(hertz[:N//2], magF[:N//2], marker='o')
plt.grid(True)
plt.xlabel('Frecvenţa (Hz)', fontsize=16, fontname='Arial')
plt.ylabel('|F(k)|', fontsize=16, fontname='Arial')
plt.title('Spectrul semnalului (doar jumătate)', fontsize=16, fontname='Arial')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
