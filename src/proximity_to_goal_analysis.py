import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyalarının yolları
positions_csv_path = "data/output/player_positions_with_teams.csv"
output_visual_path = "data/visuals/proximity_to_goal_analysis.png"

# Sol kalenin (örneğin, kale merkezi) koordinatları
goal_position = (0, 50)  # Saha boyutları normalize olduğu için (0-100 aralığında)

# CSV dosyasını yükle
df = pd.read_csv(positions_csv_path)

# "Ball" ve oyuncu verilerini filtrele
positions = df[df["Player_ID"] != "Ball"].copy()
ball_positions = df[df["Player_ID"] == "Ball"].copy()

# Mesafe hesaplama fonksiyonu
def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Oyuncuların kaleye olan uzaklıklarını hesapla
positions["Distance_to_Goal"] = positions.apply(
    lambda row: calculate_distance(row["X"] * 100, row["Y"] * 100, goal_position[0], goal_position[1]), axis=1
)

# Topun kaleye olan uzaklıklarını hesapla
ball_positions["Distance_to_Goal"] = ball_positions.apply(
    lambda row: calculate_distance(row["X"] * 100, row["Y"] * 100, goal_position[0], goal_position[1]), axis=1
)

# Oyuncuların zaman bazında kaleye olan uzaklıklarını görselleştir
plt.figure(figsize=(12, 6))
for player_id, group in positions.groupby("Player_ID"):
    plt.plot(group["Frame"], group["Distance_to_Goal"], label=f"Player {int(player_id)}")

# Topun kaleye olan uzaklıklarını zaman bazında görselleştir
plt.plot(ball_positions["Frame"], ball_positions["Distance_to_Goal"], label="Ball", linewidth=3, color="red")

# Grafik düzenlemeleri
plt.title("Oyuncular ve Topun Kaleye Yakınlık Analizi", fontsize=16)
plt.xlabel("Frame", fontsize=12)
plt.ylabel("Mesafe (Birimler)", fontsize=12)
plt.legend(loc="upper right", fontsize=10)
plt.grid(alpha=0.5)
plt.tight_layout()

# Görseli kaydet ve göster
plt.savefig(output_visual_path)
plt.show()
