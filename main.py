import matplotlib.pyplot as plt

# Data
I = [10, 20, 40, 60, 80, 100, 130, 150]
S = [79.762, 44.667, 23.929, 15.952, 13.4, 7.701, 4.187, 2.68]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(I, S, marker='o')

# Labels and Title
plt.ylabel("Smoothing Coefficient")
plt.xlabel("I (mA)")
plt.title("Smoothing Coefficient for different Current Intensity on C1RC2 filter")
plt.legend()
plt.grid(True)
plt.show()
