import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 4, 2])
b = np.array([1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 1, 1])

c = np.convolve(a, b, mode='full')

print(f"Lungimea convoluției: {len(c)}")

k = np.arange(len(c))

plt.figure(figsize=(10, 5))
plt.stem(k, c, basefmt=" ")
plt.xlabel("Index timp")
plt.ylabel("Amplitudine")
plt.title("Convoluția semnalelor a și b")
plt.grid(True)
plt.show()
