import cv2
import numpy as np
import matplotlib.pyplot as plt

#Resim okunur ve griye cevirilir
image_path = "ornek_resim.png"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Boy ve enlem alinir
height, width = gray_image.shape

#Histogramlar icin bos array olusturulur
hist = np.zeros((256,))

#Her pixel gezilir, bir arttirilarak histogram arrayinde dogru konuma kayit edilir
for y in range(height):
    for x in range(width):
        pixel_value = gray_image[y, x]
        hist[pixel_value] += 1

plt.plot(hist, color='gray')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')
plt.title('Resim Histogramı')
plt.show()
