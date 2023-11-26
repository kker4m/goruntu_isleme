import cv2
import numpy as np

# Resmi yükle (RGB formatında)
resim = cv2.imread('ornek_gorsel.jpeg', cv2.IMREAD_COLOR)
resim_rgb = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)  # BGR'den RGB'ye dönüşüm

# Otsu thresholding uygula
gray = cv2.cvtColor(resim, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Gürültüyü azaltmak için morfolojik açılım uygula
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=20)

# Konturları bul
kontur, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pirinç tanesi sayısı
rice_grain_count = len(kontur)
print(f"Pirinç tanesi sayısı: {rice_grain_count}")

# Konturları orijinal görüntüde görselleştir
result = resim_rgb.copy()
cv2.drawContours(result, kontur, -1, (0, 255, 0), 2)

# Görüntüleri göster
cv2.imshow('Thresholding Uygulanmis Resim', thresh)
cv2.imshow('Konturlar', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
