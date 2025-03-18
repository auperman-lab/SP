import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Define parameters
Ts = 0.001  # Sampling time
om0 = 2 * np.pi
dz = 0.005
A = 1
oms = om0 * Ts

# Define filter coefficients
a = [1 + 2 * dz * oms + oms**2, -2 * (1 + dz * oms), 1]
b = [A * 2 * oms**2]

# Time vector
t = np.arange(0, 50 + Ts, Ts)

# Generate white noise
x1 = np.random.rand(len(t))

# Apply second-order filter
y1 = lfilter(b, a, x1)

# Plot results
plt.plot(t, y1)
plt.grid()
plt.title('Filtrarea zgomotului cu un filtru de ordinul doi')
plt.xlabel('Timpul (s)')
plt.ylabel('Functia y(t)')
plt.show()
