import cv2
import numpy as np

goruntu = cv2.VideoCapture(0)
while True:
    ret, resim = goruntu.read()
    hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([25, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    cikti = cv2.bitwise_and(resim, resim, mask=mask)

    cv2.imshow('Orijinal Resim', resim)
    cv2.imshow('Sadece Kirmizi', cikti)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

goruntu.release()
cv2.destroyAllWindows()