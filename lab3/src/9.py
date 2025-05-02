import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 0.75  # Amplitude
Ts = 0.01  # Sampling period
T = 100    # Time duration

# Time vector
t = np.arange(0, T, Ts)

# Frequency parameters
df = 1 / T  # Frequency resolution
Fmax = 1 / Ts  # Maximum frequency
f = np.arange(0, Fmax, df)  # Frequency vector

# Function to plot the real and imaginary parts of the shifted FFT
def plot_real_imag(w):
    # Create a rectangular pulse with the current width w
    x = A * (np.abs(t % (2 * w) - w) < w / 2).astype(float)

    # Apply FFT
    y = np.fft.fft(x)

    # Shift the FFT result using fftshift
    yp = np.fft.fftshift(y)

    # Frequency vector for the shifted FFT
    f1 = np.arange(-Fmax / 2, Fmax / 2, df)

    # Plot the real and imaginary parts
    plt.figure(figsize=(10, 5))
    plt.plot(f1[:len(yp) // 2], np.real(yp)[:len(yp) // 2], label='Real Part')
    plt.plot(f1[:len(yp) // 2], np.imag(yp)[:len(yp) // 2], label='Imaginary Part')
    plt.title(f'Real and Imaginary Parts of the TF for w = {w} (Shifted)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.xlim(-np.pi, np.pi)  # Limiting x-axis to [-π, π]
    plt.show()

# Repeat for different w values
for w_value in [50, 5, 0.5]:
    plot_real_imag(w_value)
