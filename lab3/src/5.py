import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 100  # Length of the signal
T = 1 / 99  # Sampling period
t = np.arange(0, 1, T)  # Time vector

# New frequencies
f1_new = 25  # Frequency of the first sinusoid
f2_new = 50  # Frequency of the second sinusoid

# Create the new signal: sum of two sinusoids
x_new = np.sin(2 * np.pi * f1_new * t) + np.sin(2 * np.pi * f2_new * t)

# Fourier Transform for the new signal
y_new = np.fft.fft(x_new)
m_new = np.abs(y_new)  # Magnitude
p_new = np.unwrap(np.angle(y_new))  # Phase

f = np.fft.fftfreq(N, T)  # Frequency axis

# Plot Magnitude
plt.figure(figsize=(10, 5))
plt.plot(f[:N // 2], m_new[:N // 2])  # Only plot the first half (positive frequencies)
plt.title('Magnitude Spectrum (25 Hz + 50 Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xticks([f1_new, f2_new, 60, 85])
plt.grid(True)

# Plot Phase
plt.figure(figsize=(10, 5))
plt.plot(f[:N // 2], p_new[:N // 2] * 180 / np.pi)  # Phase in degrees
plt.title('Phase Spectrum (25 Hz + 50 Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.xticks([f1_new, f2_new, 60, 85])
plt.grid(True)

plt.show()
