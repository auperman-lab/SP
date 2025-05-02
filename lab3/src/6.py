import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

# Parameters
A = 0.75  # Amplitude
w = 50    # Pulse width
Ts = 0.01  # Sampling period
T = 100    # Time duration

# Time vector
t = np.arange(0, T, Ts)

# Create a rectangular pulse
x = A * (np.abs(t % (2 * w) - w) < w / 2).astype(float)

# Plot the signal using stem
plt.figure(figsize=(10, 5))
plt.stem(t, x, basefmt=" ")
plt.title('Rectangular Pulse Signal')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
