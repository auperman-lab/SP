import matplotlib.pyplot as plt

lgf = [1, 1.778, 2, 2.301, 2.602, 2.903, 3, 3.699, 4, 4.699, 5, 5.301, 5.699, 6]

Ku_EC_no_feedback = [1.82, 7.23, 11.4, 21.1, 36.3, 49.3, 52.5, 58.1, 59.1, 58.9, 56.7, 49.4, 30.8, 21.9]
Ku_EC_negative_feedback = [1.74, 4.22, 4.45, 4.58, 4.56, 4.53, 4.6, 4.55, 4.6, 4.63, 4.55, 4.49, 3.95, 4]
Ku_BC = [37.4, 78.6, 82, 83, 85.2, 86.7, 87.3, 85.7, 85, 87, 87.3, 83.9, 75.8, 70]
Ku_CC = [0.6, 0.663, 0.85, 1, 1.06, 1.1, 1.11, 1.13, 1.17, 1.1, 1.04, 1.08, 1.27, 2.04]


plt.figure(figsize=(10, 6))
plt.plot(lgf, Ku_EC_no_feedback, marker='o', label='EC fără reacție')
plt.plot(lgf, Ku_EC_negative_feedback, marker='s', label='EC reacție negativă')
plt.plot(lgf, Ku_BC, marker='^', label='BC')
plt.plot(lgf, Ku_CC, marker='d', label='CC')

# Labels and grid
plt.xlabel('frequency(Hz)')
plt.ylabel('Coeficient de amplificare $K_u$')
plt.title('Caracteristici de frecvență pentru diferite etaje amplificator')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()