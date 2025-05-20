import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = '../img/bostan.tiff'

try:
    c = cv2.imread(image_path)
    if c is None:
        raise FileNotFoundError(f"Image not found at {image_path}. Please check the path and filename.")

    c_rgb = cv2.cvtColor(c, cv2.COLOR_BGR2RGB) if len(c.shape) == 3 else c

    cc = c[0:min(c.shape[0], 256), 0:min(c.shape[1], 256)] if c.shape[0] < 256 or c.shape[1] < 256 else c[50:306, 206:462]
    if c.shape[0] < 256 or c.shape[1] < 256:
        print("Warning: Image is smaller than 256x256. Cropping will be limited by image dimensions.")

    cc_rgb = cv2.cvtColor(cc, cv2.COLOR_BGR2RGB) if len(cc.shape) == 3 else cc
    cc_float = cc.astype(np.float32)

    max_pixel_value = np.max(cc_float)
    if max_pixel_value == 0:
        c_log = 0
    else:
        c_log = 255 / np.log(1 + max_pixel_value)

    c1_log_transformed = c_log * np.log(1 + cc_float)

    # Clip values to 0-255 range and convert to uint8
    c1 = np.clip(c1_log_transformed, 0, 255).astype(np.uint8)

    c1_rgb = cv2.cvtColor(c1, cv2.COLOR_BGR2RGB) if len(c1.shape) == 3 else c1

    plt.figure()
    plt.imshow(c1_rgb)
    plt.title('Image after Logarithmic Scaling')
    plt.axis('off')

    plt.show()

except FileNotFoundError as e:
    print(e)
    print("Please make sure 'your_image_name.tif' exists and the path is correct.")
except Exception as e:
    print(f"An error occurred: {e}")