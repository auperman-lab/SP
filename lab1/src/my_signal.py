import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 50
m = np.arange(0, R)
s = 2 * m * (0.9 ** m)

# Create the stem plot
plt.stem(m, s, basefmt=" ")
plt.grid(True)

# Set font properties
plt.xlabel('Indecsul de timp n', fontsize=16, family='Arial')
plt.ylabel('Amplitudinea', fontsize=16, family='Arial')
plt.title('Semnalul original', fontsize=16, family='Arial')

# Display the plot
plt.show()
