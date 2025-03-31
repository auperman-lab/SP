import numpy as np
import matplotlib.pyplot as plt
import time

n = np.arange(0, 262144)
l = np.arange(0, 262144)

a = 2 * np.sign(np.sin(20 * np.pi * n + 1))
b = 3 * (np.mod(n / 65536, 1) - 0.5)

start_time = time.time()
c = np.convolve(a, b, mode='full')
time_convolution_direct = time.time() - start_time
print(f"Timpul pentru convoluția directă: {time_convolution_direct:.6f} secunde")

m = len(a) + len(b) - 1
m = 2 ** int(np.ceil(np.log2(m)))

start_time = time.time()
AE = np.fft.fft(a, m)
BE = np.fft.fft(b, m)
p = AE * BE
y1 = np.fft.ifft(p)
time_convolution_fft = time.time() - start_time
print(f"Timpul pentru convoluția cu FFT: {time_convolution_fft:.6f} secunde")

c_trimmed = c[:m]

error = np.real(c_trimmed) - np.real(y1[:len(c_trimmed)])

k = np.arange(len(c_trimmed))  # Adjust k to have the same length as c_trimmed and y1

plt.figure(figsize=(10, 10))

plt.subplot(3, 1, 1)
plt.plot(k, np.real(c_trimmed))
plt.xlabel("Index timp")
plt.ylabel("Amplitudine")
plt.title("Convoluția Directă")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(k, np.real(y1[:len(c_trimmed)]))
plt.xlabel("Index timp")
plt.ylabel("Amplitudine")
plt.title("Convoluția Obținută prin FFT")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(k, error)
plt.xlabel("Index timp")
plt.ylabel("Eroare")
plt.title("Eroarea între Convoluția Directă și FFT")
plt.grid(True)

plt.tight_layout()
plt.show()

print(f"Timpul total pentru convoluția directă: {time_convolution_direct:.6f} secunde")
print(f"Timpul total pentru convoluția cu FFT: {time_convolution_fft:.6f} secunde")
