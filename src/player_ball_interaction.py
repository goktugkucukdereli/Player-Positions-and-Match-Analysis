import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasını yükle
csv_path = "data/output/player_positions.csv"
df = pd.read_csv(csv_path)

# Top pozisyonları
ball_positions = df[df["Player_ID"] == "Ball"]

# Oyuncu pozisyonları
player_positions = df[df["Player_ID"] != "Ball"]

# Oyuncu-top mesafelerini hesapla
closest_players = []
for frame in ball_positions["Frame"].unique():
    ball_data = ball_positions[ball_positions["Frame"] == frame]
    player_data = player_positions[player_positions["Frame"] == frame]
    
    if not ball_data.empty and not player_data.empty:
        ball_x, ball_y = ball_data.iloc[0]["X"], ball_data.iloc[0]["Y"]
        player_data["Distance"] = np.sqrt((player_data["X"] - ball_x)**2 + (player_data["Y"] - ball_y)**2)
        closest_player = player_data.loc[player_data["Distance"].idxmin()]
        closest_players.append([frame, closest_player["Player_ID"], closest_player["Distance"]])

# En yakın oyuncular DataFrame'i
closest_df = pd.DataFrame(closest_players, columns=["Frame", "Closest_Player_ID", "Distance"])

# En yakın oyuncuların dağılımını görselleştir
closest_counts = closest_df["Closest_Player_ID"].value_counts()

plt.figure(figsize=(12, 6))
closest_counts.plot(kind="bar", color="lightgreen", edgecolor="black")
plt.title("Topa En Yakın Oyuncular", fontsize=16)
plt.xlabel("Oyuncu ID", fontsize=12)
plt.ylabel("Yakınlık Sayısı", fontsize=12)
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Grafiği kaydet ve göster
plt.show()
