import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
from matplotlib.animation import FuncAnimation

# CSV dosyasını yükle
positions_csv_path = "data/output/player_positions_with_teams.csv"
df = pd.read_csv(positions_csv_path)

# Boş değerleri temizle
df.dropna(inplace=True)

# Zaman dilimini seç (örnek olarak ilk 100 kare)
time_range = df["Frame"].unique()[:100]  # İlk 100 kareyi seçiyoruz
df_time_filtered = df[df["Frame"].isin(time_range)]

# Saha çizimi
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw()
scatter_players = pitch.scatter([], [], s=200, color="blue", edgecolor="black", label="Players", ax=ax)
scatter_ball = pitch.scatter([], [], s=300, color="red", label="Ball", ax=ax)

# Animasyonu güncelleme fonksiyonu
def update(frame):
    current_frame_data = df_time_filtered[df_time_filtered["Frame"] == frame]
    players_data = current_frame_data[current_frame_data["Player_ID"] != "Ball"]
    ball_data = current_frame_data[current_frame_data["Player_ID"] == "Ball"]

    # Oyuncu pozisyonlarını güncelle
    scatter_players.set_offsets(players_data[["X", "Y"]].values * 100)

    # Top pozisyonunu güncelle
    if not ball_data.empty:
        scatter_ball.set_offsets(ball_data[["X", "Y"]].values * 100)
    else:
        scatter_ball.set_offsets([])

    ax.set_title(f"Zaman Bazlı Hareket - Kare {frame}", fontsize=16)

# Animasyonu oluştur
animation = FuncAnimation(fig, update, frames=time_range, interval=200)

# Animasyonu kaydetmek için (isteğe bağlı):
animation.save("data/visuals/time_based_movement_analysis.mp4", fps=5, dpi=200)

# Animasyonu göstermek için:
plt.legend(loc="upper right")
plt.show()
