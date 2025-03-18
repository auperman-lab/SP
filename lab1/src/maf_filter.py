import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth


# Parameters
R = 50
M = 100
m = np.arange(0, R, 0.001)
# s = 2 * m * (0.9 ** m)

s = 2 * sawtooth( 3*np.pi*m +np.pi/6)

d = np.random.rand(len(m)) - 0.5

x = s + d

b = np.ones(M) / M

y = np.convolve(x, b, mode='same')

plt.plot(m, s, label='Semnalul original')
plt.plot(m, x, label='Semnalul cu zgomot')
plt.plot(m, y, label='Semnalul filtrat')

plt.xlabel('Indecsul de timp n', fontsize=16, family='Arial')
plt.ylabel('Amplitudinea', fontsize=16, family='Arial')
plt.title('Semnalul original, zgomotul si semnalul filtrat', fontsize=16, family='Arial')

plt.grid(True)
plt.legend()

plt.show()
