import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 50
m = np.arange(0, R)
s = 2 * m * (0.9 ** m)

d = np.random.rand(len(m)) - 0.5

s_noisy = s + d

plt.plot(m, s, label='Semnalul original')
plt.plot(m, s_noisy, label='Semnalul cu zgomot')

plt.xlabel('Indecsul de timp n', fontsize=16, family='Arial')
plt.ylabel('Amplitudinea', fontsize=16, family='Arial')
plt.title('Semnalul original si semnalul cu zgomot', fontsize=16, family='Arial')

plt.grid(True)
plt.legend()

plt.show()
