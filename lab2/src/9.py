import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 4, 2])
b = np.array([1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 1, 1])

b1 = b[:6]
b2 = b[6:]

c1 = np.convolve(a, b1, mode='full')
c2 = np.convolve(a, b2, mode='full')

k1 = np.arange(len(c1))
k2 = np.arange(len(c2))

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.stem(k1, c1, basefmt=" ")
plt.xlabel("Index timp")
plt.ylabel("Amplitudine")
plt.title("Convoluția primului bloc (c1)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(k2, c2, basefmt=" ")
plt.xlabel("Index timp")
plt.ylabel("Amplitudine")
plt.title("Convoluția celui de-al doilea bloc (c2)")
plt.grid(True)

plt.tight_layout()
plt.show()

print(f"Lungimea convoluției primului bloc: {len(c1)}")
print(f"Lungimea convoluției celui de-al doilea bloc: {len(c2)}")
