import numpy as np
import matplotlib.pyplot as plt

a = np.array([-2, 0, 1, -1, 3])
b = np.array([1, 2, 0, -1])

n = np.arange(1, len(a) + 1)
m = np.arange(1, len(b) + 1)


fig, axs = plt.subplots(2, 1, figsize=(6, 6))

axs[0].stem(n, a,linefmt="k", basefmt=" ")
axs[0].set_xlabel('Indexul de timp n')
axs[0].set_ylabel('Amplitudine')
axs[0].set_title('Secventa a')
axs[0].grid(True)

axs[1].stem(m, b,linefmt="k", basefmt=" ")
axs[1].set_xlabel('Indexul de timp m')
axs[1].set_ylabel('Amplitudine')
axs[1].set_title('Secventa b')
axs[1].grid(True)

plt.tight_layout()
plt.show()
