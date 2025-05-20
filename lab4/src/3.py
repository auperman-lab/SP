import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

# Define the image path
image_path = '../img/bostan.tiff'

try:
    # 1. Load and prepare the image
    c = cv2.imread(image_path)
    if c is None:
        raise FileNotFoundError(f"Image not found at {image_path}. Please check the path and filename.")

    c_rgb = cv2.cvtColor(c, cv2.COLOR_BGR2RGB) if len(c.shape) == 3 else c

    if c.shape[0] < 256 or c.shape[1] < 256:
        print("Warning: Image is smaller than 256x256. Cropping will be limited by image dimensions.")
        cc = c[0:min(c.shape[0], 256), 0:min(c.shape[1], 256)]
    else:
        cc = c[50:306, 206:462]

    cc_rgb = cv2.cvtColor(cc, cv2.COLOR_BGR2RGB) if len(cc.shape) == 3 else cc

    is_color = len(cc.shape) == 3

    if is_color:
        IG = cv2.cvtColor(cc, cv2.COLOR_BGR2GRAY)
    else:
        IG = cc.copy() # Use a copy if it's already grayscale


    kernel_3x3 = np.ones((3, 3), np.float32) / (3 * 3)

    cf1_3x3_gray = cv2.filter2D(IG, -1, kernel_3x3)

    plt.imshow(cf1_3x3_gray, cmap='gray')
    plt.title('Filtered (3x3 Avg)')
    plt.axis('off')
    plt.suptitle('Filtering with a 3x3 Average Filter')
    plt.show()


    kernel_5x7 = np.ones((5, 7), np.float32) / (5 * 7)

    cf1_5x7_gray = cv2.filter2D(IG, -1, kernel_5x7)

    plt.imshow(cf1_5x7_gray, cmap='gray')
    plt.title('Filtered (5x7 Avg)')
    plt.axis('off')
    plt.suptitle('Filtering with a 5x7 Average Filter')
    plt.show()


    kernel_11x11 = np.ones((11, 11), np.float32) / (11 * 11)

    cf1_11x11_gray = cv2.filter2D(IG, -1, kernel_11x11)


    plt.imshow(cf1_11x11_gray, cmap='gray')
    plt.title('Filtered (11x11 Avg)')
    plt.axis('off')
    plt.suptitle('Filtering with an 11x11 Average Filter')
    plt.show()



    laplacian_kernel = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]], dtype=np.float32)
    cf2_laplacian = cv2.filter2D(IG, cv2.CV_32F, laplacian_kernel)
    cf2_laplacian = np.uint8(np.clip(np.abs(cf2_laplacian), 0, 255))

    sigma_log = 1.0
    ksize_log = int(2 * np.ceil(2 * sigma_log) + 1)
    if ksize_log % 2 == 0: ksize_log += 1

    gaussian_blur_log = cv2.GaussianBlur(IG, (ksize_log, ksize_log), sigma_log)
    cf3_log = cv2.Laplacian(gaussian_blur_log, cv2.CV_32F)
    cf3_log = np.uint8(np.clip(np.abs(cf3_log), 0, 255))

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cf2_laplacian, cmap='gray')
    plt.title('Laplacian Filter')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cf3_log, cmap='gray')
    plt.title(' Laplacian of Gaussian (LoG)')
    plt.axis('off')
    plt.suptitle('Edge Detection')
    plt.show()



    def add_salt_and_pepper_noise(image, density=0.05):
        noisy_image = np.copy(image)
        total_pixels = image.size if len(image.shape) == 2 else image.shape[0] * image.shape[1]
        num_salt = int(total_pixels * density / 2)
        num_pepper = int(total_pixels * density / 2)

        coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
        if len(image.shape) == 2: # Grayscale
            noisy_image[coords[0], coords[1]] = 255
        else: # Color (apply to all channels)
            noisy_image[coords[0], coords[1], :] = 255

        coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
        if len(image.shape) == 2: # Grayscale
            noisy_image[coords[0], coords[1]] = 0
        else: # Color (apply to all channels)
            noisy_image[coords[0], coords[1], :] = 0
        return noisy_image

    c_sp_gray = add_salt_and_pepper_noise(IG, density=0.05)

    plt.figure(figsize=(6, 6))
    plt.imshow(c_sp_gray, cmap='gray')
    plt.title('Image with Salt & Pepper Noise')
    plt.axis('off')
    plt.show()



    kernel_a3 = np.ones((3, 3), np.float32) / (3 * 3)
    c_sp_f3 = cv2.filter2D(c_sp_gray, -1, kernel_a3)

    plt.subplot(1, 2, 2)
    plt.imshow(c_sp_f3, cmap='gray')
    plt.title('Filtered with 5x7 Average')
    plt.axis('off')
    plt.suptitle('Filtering Salt & Pepper Noisy Image')
    plt.show()


except FileNotFoundError as e:
    print(e)
    print("Please make sure 'bostan.tiff' exists and the path is correct.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")