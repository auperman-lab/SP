import matplotlib.pyplot as plt
import numpy as np

# Data from your experiment
# voltage = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45]  # for direct polarization 1st diode
# voltage = [0.00, 0.10, 0.30, 0.50, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85]  # for direct polarization 2nd  and 3rd diode
# voltage = [0.0, -0.5, -1.0, -1.1, -1.2, -1.3, -1.4, -1.5, -1.6, -1.7, -1.8, -1.9, -2]  # for direct polarization 2nd  and 3rd diode

# voltage = [ -1, -3, -5, -10, -15, -20, -25, -30]  # for inverse polarization 1st and 2nd diode
voltage = [0.0, -5.0, -7.0, -7.37, -7.39, -7.42, -7.46, -7.5, -7.54, -7.58, -7.61, -7.65]  # for inverse polarization 3rd diode



# current = [5e-5, 0.0795, 0.371, 1.171, 3.0, 6.225, 11.066, 16.78, 23.5, 30]  # for direct polarization 1st diode
# current = [0, 0.000042, 0.001904, 0.0983, 0.72, 1936, 4926, 11163, 21200, 37115] # for direct polarization 2nd diode
# current = [0, 0.000036, 0.00003, 0.00049, 0.0114, 0.0664, 0.403, 2400, 9840, 26000] # for direct polarization 3rd diode
# current = [0.000, -0.000044, -0.000095, -0.000099, -0.000113, -0.000147, -0.00032, -0.00156, -0.010, -0.085, -0.774, -3252, -8206] # for direct polarization 4th diode

# current = [ -0.00214, -0.0025, -0.00285, -0.00368, -0.00447, -0.00532, -0.00632, -0.0076] # for inverse polarization 1st diode
# current = [-0.000093, -0.000274, -0.000454, -0.00099, -0.00149, -0.00198, -0.00247, -0.00297] # for inverse polarization 2nd diode
current = [0, -0.492, -0.919, -1, -2, -5, -10, -15, -20, -25, -30, -35]  # for inverse polarization 3rd diode

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(voltage,current, marker='o', linestyle='-', color='b', label='Direct I-V characteristic')

ax.set_xlabel("Voltage (V)", fontsize=12)
ax.set_ylabel("Current (mA)", fontsize=12)
ax.grid(True)
plt.title("I-V Characteristics of a Semiconductor Diode (Direct)", fontsize=14)

# Show plot
plt.show()
