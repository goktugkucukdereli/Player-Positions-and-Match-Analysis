import cv2
import mediapipe as mp
import csv
import os

# Mediapipe Pose modeli
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False)

# Karelerin bulunduğu klasör ve CSV çıktısı
frames_folder = "data/frames/"
output_csv = "data/output/player_positions.csv"

# HSV renk aralığı (beyaz top için)
lower_white = (0, 0, 200)
upper_white = (180, 30, 255)

# CSV başlıkları
header = ["Frame", "Player_ID", "X", "Y"]

# CSV dosyasını oluştur
with open(output_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    # Kareleri işleme
    for frame_file in sorted(os.listdir(frames_folder)):
        if not frame_file.endswith(".jpg"):
            continue
        
        frame_path = os.path.join(frames_folder, frame_file)
        frame_number = int(frame_file.split("_")[1].split(".")[0])  # Örneğin: frame_30.jpg
        
        # Görüntüyü yükle
        image = cv2.imread(frame_path)
        if image is None:
            print(f"Error: {frame_path} yüklenemedi.")
            continue

        # Mediapipe ile oyuncu tespiti
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            player_id = 1  # Varsayılan bir Player_ID, her landmark bir oyuncu olabilir
            for landmark in results.pose_landmarks.landmark:
                x = landmark.x
                y = landmark.y
                writer.writerow([frame_number, player_id, x, y])
                player_id += 1
        else:
            print(f"Oyuncu tespit edilemedi: {frame_path}")

        # HSV renk uzayına çevir ve topu tespit et
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_image, lower_white, upper_white)

        # Konturları bul ve en büyük konturu seç
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            ball_x = (x + x + w) / 2 / image.shape[1]  # Normalize edilmiş X
            ball_y = (y + y + h) / 2 / image.shape[0]  # Normalize edilmiş Y
            writer.writerow([frame_number, "Ball", ball_x, ball_y])
        else:
            print(f"Top tespit edilemedi: {frame_path}")
