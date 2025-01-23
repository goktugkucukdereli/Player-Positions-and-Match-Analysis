import cv2
import pandas as pd
import numpy as np
from mplsoccer import Pitch
import matplotlib.pyplot as plt

# Video ve CSV yolları
video_path = "data/videos/argentina-france_final.mp4"  # Orijinal video yolu
positions_csv_path = "data/output/player_positions.csv"  # Oyuncu pozisyon verileri
output_video_path = "data/videos/output_with_analysis.mp4"  # Çıkış videosu

# CSV verisini yükle
df = pd.read_csv(positions_csv_path)
df = df.dropna()  # Boş satırları temizle
df = df[df["Player_ID"] != "Ball"]  # "Ball" değerlerini filtrele
df["Player_ID"] = df["Player_ID"].astype(int)  # Player_ID'yi tam sayıya çevir

# Video yükle
cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Sahayı çizen Pitch objesi
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')

# Frame bazlı işleme
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Şu anki frame ile eşleşen pozisyonları seç
    current_positions = df[df["Frame"] == frame_count]

    # OpenCV görüntüsünü Matplotlib figürüne dönüştür
    fig, ax = pitch.draw(figsize=(16, 9))
    for _, row in current_positions.iterrows():
        x, y, player_id = row["X"] * 100, row["Y"] * 100, int(row["Player_ID"])
        pitch.scatter(x, y, ax=ax, s=300, label=f"Player {player_id}", alpha=0.6)

    # Matplotlib figürünü OpenCV formatına dönüştür
    fig.canvas.draw()
    overlay = np.array(fig.canvas.renderer.buffer_rgba())
    overlay = cv2.cvtColor(overlay, cv2.COLOR_RGBA2BGR)  # RGBA -> BGR
    overlay = cv2.resize(overlay, (frame_width, frame_height))  # Boyutları eşitle

    # OpenCV frame ile birleştir
    combined_frame = cv2.addWeighted(frame, 0.7, overlay, 0.3, 0)

    # Çıkış videosuna yaz
    out.write(combined_frame)

    # Matplotlib figürünü kapat
    plt.close(fig)

    frame_count += 1
    print(f"Processing frame {frame_count}", end="\r")

cap.release()
out.release()
print(f"Video analizi tamamlandı. Çıktı videosu: {output_video_path}")
