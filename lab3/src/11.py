import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

Ts = 0.01
T = 50
t = np.arange(0, T + Ts, Ts)

x1 = np.random.rand(len(t))

dz = 0.05
A = 1
om0 = 2 * np.pi
oms = om0 * Ts

a = [1 + 2 * dz * oms + oms**2,
     -2 * (1 + dz * oms),
     1]
b = [A * 2 * dz * oms**2]

b = b + [0, 0]

y1 = lfilter(b, a, x1)

# Afișare rezultat filtrat
plt.figure(figsize=(12, 4))
plt.plot(t, y1)
plt.title('Zgomot alb filtrat')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()
