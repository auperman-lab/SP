import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

image_path = '../img/bostan.tiff'

try:
    c = cv2.imread(image_path)
    if c is None:
        raise FileNotFoundError(f"Image not found at {image_path}. Please check the path and filename.")

    if c.shape[0] < 256 or c.shape[1] < 256:
        print("Warning: Image is smaller than 256x256. Cropping will be limited by image dimensions.")
        cc = c[0:min(c.shape[0], 256), 0:min(c.shape[1], 256)]
    else:
        cc = c[50:306, 206:462]

    IG = cv2.cvtColor(cc, cv2.COLOR_BGR2GRAY)


    a = np.zeros((256, 256), dtype=np.uint8)
    a[78:178, 78:178] = 255

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(a, cmap='gray')
    plt.title(' Generated Square Image')
    plt.axis('off')

    af_complex = np.fft.fftshift(np.fft.fft2(a))
    af_magnitude = 20 * np.log(np.abs(af_complex) + 1)

    plt.subplot(1, 2, 2)
    plt.imshow(af_magnitude, cmap='gray')
    plt.title(' Fourier Spectrum (Magnitude)')
    plt.axis('off')
    plt.suptitle(' Geometric Figure and Fourier Spectrum')
    plt.show()



    def add_salt_and_pepper_noise(image, density=0.05):
        noisy_image = np.copy(image)
        total_pixels = image.size if len(image.shape) == 2 else image.shape[0] * image.shape[1]
        num_salt = int(total_pixels * density / 2)
        num_pepper = int(total_pixels * density / 2)

        coords_salt_row = np.random.randint(0, image.shape[0] - 1, num_salt)
        coords_salt_col = np.random.randint(0, image.shape[1] - 1, num_salt)
        if len(image.shape) == 2: # Grayscale
            noisy_image[coords_salt_row, coords_salt_col] = 255
        else:
            noisy_image[coords_salt_row, coords_salt_col, :] = 255

        coords_pepper_row = np.random.randint(0, image.shape[0] - 1, num_pepper)
        coords_pepper_col = np.random.randint(0, image.shape[1] - 1, num_pepper)
        if len(image.shape) == 2: # Grayscale
            noisy_image[coords_pepper_row, coords_pepper_col] = 0
        else:
            noisy_image[coords_pepper_row, coords_pepper_col, :] = 0
        return noisy_image

    c_sp = add_salt_and_pepper_noise(IG, density=0.05)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(c_sp, cmap='gray')
    plt.title(' Image with Salt & Pepper Noise')
    plt.axis('off')

    cf_complex = np.fft.fftshift(np.fft.fft2(c_sp))
    cf_magnitude = 20 * np.log(np.abs(cf_complex) + 1) # Log scale for visualization

    plt.subplot(1, 2, 2)
    plt.imshow(cf_magnitude, cmap='gray')
    plt.title(' Fourier Spectrum of Noisy Image')
    plt.axis('off')
    plt.suptitle(' Noisy Image and Fourier Spectrum')
    plt.show()


    low_pass_mask = a.astype(np.float32) / 255.0

    cf1_filtered_complex = cf_complex * low_pass_mask

    cf1_filtered_magnitude = 20 * np.log(np.abs(cf1_filtered_complex) + 1)

    plt.figure(figsize=(6, 6))
    plt.imshow(cf1_filtered_magnitude, cmap='gray')
    plt.title(' Filtered Spectrum (Low-Pass)')
    plt.axis('off')
    plt.show()



    cf2_filtered_image = np.fft.ifft2(np.fft.ifftshift(cf1_filtered_complex)).real

    cf2_display = np.clip(cf2_filtered_image, 0, 255).astype(np.uint8)

    plt.figure(figsize=(6, 6))
    plt.imshow(cf2_display, cmap='gray')
    plt.title('Reconstructed Image after Low-Pass Filtering')
    plt.axis('off')
    plt.show()


except FileNotFoundError as e:
    print(e)
    print("Please make sure 'bostan.tiff' exists and the path is correct.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")