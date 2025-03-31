import numpy as np
import matplotlib.pyplot as plt

# Semnalele
a = np.array([1, 4, 2])
b = np.array([1, 2, 3, 4, 5, 4, 3, 3, 2, 2, 1, 1])

b1 = b[:6]
b2 = b[6:]

c1 = np.convolve(a, b1, mode='full')
c2 = np.convolve(a, b2, mode='full')

c_add = np.concatenate([c1[:6], c1[6:8] + c2[:2], c2[2:]])

m = np.arange(len(c_add))

plt.figure(figsize=(8, 4))
plt.stem(m, c_add, basefmt=" ")
plt.xlabel("Index timp")
plt.ylabel("Amplitudine")
plt.title("Convoluția finală (c_add)")
plt.grid(True)
plt.show()

print(f"Convoluția finală: {c_add}")
print(f"Lungimea convoluției finale: {len(c_add)}")
