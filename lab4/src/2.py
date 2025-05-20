import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the image path
image_path = '../img/bostan.tiff'

try:
    c = cv2.imread(image_path)
    if c is None:
        raise FileNotFoundError(f"Image not found at {image_path}. Please check the path and filename.")

    c_rgb = cv2.cvtColor(c, cv2.COLOR_BGR2RGB) if len(c.shape) == 3 else c

    cc = c[50:306, 206:462]

    cc_rgb = cv2.cvtColor(cc, cv2.COLOR_BGR2RGB) if len(cc.shape) == 3 else cc


    colors = ('b', 'g', 'r')
    for i, color in enumerate(colors):
        hist = cv2.calcHist([cc], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, alpha=0.7)
    plt.title('Histograms (Color Channels)')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.legend(['Blue channel', 'Green channel', 'Red channel'])
    plt.grid(True)
    plt.show()


    b, g, r = cv2.split(cc)

    b_eq = cv2.equalizeHist(b)
    g_eq = cv2.equalizeHist(g)
    r_eq = cv2.equalizeHist(r)

    h_color = cv2.merge([b_eq, g_eq, r_eq])
    h_color_rgb = cv2.cvtColor(h_color, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(cc_rgb)
    plt.title('Original Color Image (cc)')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(h_color_rgb)
    plt.title('Equalized Color Image (h)')
    plt.axis('off')
    plt.show()


    colors_eq = ('b', 'g', 'r')
    for i, color in enumerate(colors_eq):
        hist_eq = cv2.calcHist([h_color], [i], None, [256], [0, 256])
        plt.plot(hist_eq, color=color, alpha=0.7)
    plt.title('Histograms of Equalized Color')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.legend(['Blue channel (Equalized)', 'Green channel (Equalized)', 'Red channel (Equalized)'])
    plt.grid(True)
    plt.tight_layout()
    plt.show()

except FileNotFoundError as e:
    print(e)
    print("Please make sure 'bostan.tiff' exists and the path is correct.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")