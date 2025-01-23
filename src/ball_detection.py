import cv2
import numpy as np

# Örnek bir kare üzerinde çalışma
frame_path = "data/frames/frame_30.jpg"  # Örnek kare dosyası
image = cv2.imread(frame_path)

# HSV renk uzayına çevirme
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Beyaz renk için maske oluşturma
lower_white = np.array([0, 0, 200])  # Beyazın alt sınırı
upper_white = np.array([180, 30, 255])  # Beyazın üst sınırı
mask = cv2.inRange(hsv_image, lower_white, upper_white)

# Maskeyi görüntüleme
cv2.imshow("Ball Detection", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
