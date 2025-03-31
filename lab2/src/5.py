import numpy as np
import matplotlib.pyplot as plt

a = np.array([-2, 0, 1, -1, 3])
b = np.array([1, 2, 0, -1])

c = np.convolve(a, b, mode='full')

m = len(a) + len(b) - 1

AE = np.fft.fft(a, m)
BE = np.fft.fft(b, m)

p = AE * BE

y1 = np.fft.ifft(p)

error = np.real(c[:m]) - np.real(y1)

k = np.arange(m)

plt.figure(figsize=(6, 6))

# Convoluția inițială
plt.subplot(3, 1, 1)
plt.stem(k, np.real(c[:m]), basefmt=" ")
plt.xlabel("Index timp")
plt.ylabel("Amplitudine")
plt.title("Convoluția Inițială")
plt.grid(True)

# Convoluția obținută prin FFT
plt.subplot(3, 1, 2)
plt.stem(k, np.real(y1), basefmt=" ")
plt.xlabel("Index timp")
plt.ylabel("Amplitudine")
plt.title("Convoluția obținută prin FFT")
plt.grid(True)

# Eroarea
plt.subplot(3, 1, 3)
plt.stem(k, error, basefmt=" ")
plt.xlabel("Index timp")
plt.ylabel("Eroare")
plt.title("Eroarea între convoluția inițială și cea obținută")
plt.grid(True)

# Afișarea graficului
plt.tight_layout()
plt.show()
