import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 64
T = 1 / 128  # Sampling period
k = np.arange(N)
freqs_to_test = [10, 30, 60, 70, 90, 118]

plt.figure(figsize=(15, 12))

for i, freq in enumerate(freqs_to_test):
    # Generate the signal
    f = np.sin(2 * np.pi * freq * k * T)

    # Compute the DFT
    F = np.fft.fft(f)

    # Plot the magnitude spectrum
    plt.subplot(3, 2, i + 1)
    plt.plot(k, np.abs(F), marker='o')
    plt.grid(True)
    plt.title(f'Frecvenţa semnalului = {freq} Hz', fontsize=14, fontname='Arial')
    plt.xlabel('k (indice în domeniul frecvenţei)', fontsize=12, fontname='Arial')
    plt.ylabel('|F(k)|', fontsize=12, fontname='Arial')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

plt.tight_layout()
plt.show()
