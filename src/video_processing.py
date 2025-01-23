import cv2
import os

# Video dosyasının yolu
video_path = "data/videos/argentina-france_final.mp4"  # İndirdiğiniz video dosyası
output_dir = "data/frames"  # Karelerin kaydedileceği klasör
os.makedirs(output_dir, exist_ok=True)

# Video dosyasını aç
cap = cv2.VideoCapture(video_path)

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Her 30. kareyi kaydet (1 saniyede 30 kare varsayılarak)
    if frame_count % 30 == 0:
        frame_name = os.path.join(output_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_name, frame)

    frame_count += 1

cap.release()
cv2.destroyAllWindows()
print(f"{frame_count} kare işlendi.")
