import cv2
import mediapipe as mp

# Mediapipe modelleri
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Örnek bir kare üzerinde çalışma
frame_path = "data/frames/frame_390.jpg"  # Örnek kare dosyası
image = cv2.imread(frame_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Oyuncuları tespit et
results = pose.process(image_rgb)

# Tespit edilen pozisyonları çiz
if results.pose_landmarks:
    for landmark in results.pose_landmarks.landmark:
        x = int(landmark.x * image.shape[1])
        y = int(landmark.y * image.shape[0])
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

# Sonucu göster
cv2.imshow("Player Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
