import numpy as np
import matplotlib.pyplot as plt

a = np.array([-2, 0, 1, -1, 3])
b = np.array([1, 2, 0, -1])

m = len(a) + len(b) - 1

AE = np.fft.fft(a, m)
BE = np.fft.fft(b, m)

p = AE * BE

y1 = np.fft.ifft(p)

plt.figure(figsize=(6, 4))
plt.stem(np.arange(m), np.real(y1), basefmt=" ")
plt.xlabel("Index timp")
plt.ylabel("Amplitudine")
plt.title("Convoluția a(n) * b(n) obținută prin IFFT")
plt.grid(True)
plt.show()
