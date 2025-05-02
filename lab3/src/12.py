import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Parametri
Ts = 0.01
T = 50
t = np.arange(0, T + Ts, Ts)

# Semnal de zgomot alb
x1 = np.random.rand(len(t))

# Parametrii filtrului
dz = 0.05
A = 1
om0 = 2 * np.pi
oms = om0 * Ts

# Coeficienți filtru
a = [1 + 2 * dz * oms + oms**2, -2 * (1 + dz * oms), 1]
b = [A * 2 * dz * oms**2, 0, 0]  # completăm cu zerouri pentru ordinul a

# Aplicare filtru
y1 = lfilter(b, a, x1)

# Transformata Fourier
Fu1 = np.fft.fft(x1)
Fu2 = np.fft.fft(y1)

# Centrare spectru (fftshift)
Fu1p = np.fft.fftshift(Fu1)
Fu2p = np.fft.fftshift(Fu2)

# Magnitudine
m = np.abs(Fu1p)
m1 = np.abs(Fu2p)

# Vectorul frecvențelor
df = 1 / T
Fmax = 1 / Ts
N = len(t)
f = np.linspace(-Fmax / 2, Fmax / 2, N)

# Afișare spectru intrare (zgomot alb)
plt.figure(figsize=(12, 4))
plt.stem(f, m, basefmt=" ")
plt.title("Spectrul zgomotului alb (intrare)")
plt.xlabel("Frecvența (Hz)")
plt.ylabel("Magnitudine")
plt.grid(True)

# Afișare spectru ieșire (zgomot filtrat)
plt.figure(figsize=(12, 4))
plt.stem(f, m1, basefmt=" ")
plt.title("Spectrul semnalului filtrat (ieșire)")
plt.xlabel("Frecvența (Hz)")
plt.ylabel("Magnitudine")
plt.grid(True)

plt.show()
