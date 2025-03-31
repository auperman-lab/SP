import numpy as np
import matplotlib.pyplot as plt

# Definirea secvențelor
a = np.array([-2, 0, 1, -1, 3])
b = np.array([1, 2, 0, -1])

# Calculul convoluției
c = np.convolve(a, b, mode='full')

# Definirea axei de timp
k = np.arange(1, len(c) + 1)  # Index de la 1 la 8

# Afișarea rezultatului convoluției
plt.figure(figsize=(6, 4))
plt.stem(k, c, linefmt="k", markerfmt="ko", basefmt=" ")
plt.xlabel('Indexul de timp k')
plt.ylabel('Amplitudine')
plt.title('Convoluția secvențelor a și b')
plt.grid(True)
plt.show()
