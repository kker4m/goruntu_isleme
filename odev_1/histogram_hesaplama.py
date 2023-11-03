import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "ornek_resim.png"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

height, width, _ = image.shape


hist = np.zeros((256,))


for y in range(height):
    for x in range(width):
        pixel_value = image[y, x, 0]
        hist[pixel_value] += 1

plt.plot(hist, color='gray')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')
plt.title('Resim Histogramı')
plt.show()
