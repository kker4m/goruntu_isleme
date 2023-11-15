import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv_gorsel = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_kirmizi = np.array([0, 100, 100])
    up_kirmizi = np.array([10, 255, 255])

    aralik = cv2.inRange(hsv_gorsel, low_kirmizi, up_kirmizi)
    ters_aralik = 255 - aralik

    result = cv2.bitwise_and(frame, frame, mask=aralik)

    cv2.imshow('Kamera goruntusu', frame)
    cv2.imshow('Cikti', result)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
