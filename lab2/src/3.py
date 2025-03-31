import numpy as np
import matplotlib.pyplot as plt

a = np.array([-2, 0, 1, -1, 3])
b = np.array([1, 2, 0, -1])

m = len(a) + len(b) - 1

AE = np.fft.fft(a, m)
BE = np.fft.fft(b, m)

p = AE * BE

k = np.arange(m)

plt.figure(figsize=(6, 4))
plt.stem(k, np.abs(p), basefmt=" ")
plt.xlabel("Frecvența k")
plt.ylabel("Amplitudine")
plt.title("Produsul Transformărilor Fourier ale a(n) și b(n)")
plt.grid(True)
plt.show()
