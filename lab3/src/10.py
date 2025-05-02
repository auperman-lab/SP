import numpy as np
import matplotlib.pyplot as plt

# Parametri
Ts = 0.01  # Perioada de eşantionare
T = 50     # Durata totală
t = np.arange(0, T + Ts, Ts)  # Vectorul de timp

# Generarea zgomotului alb (valori aleatoare între 0 și 1)
x1 = np.random.rand(len(t))

# Afişarea semnalului zgomotos
plt.figure(figsize=(12, 4))
plt.plot(t, x1)
plt.title('Zgomot alb')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.show()
