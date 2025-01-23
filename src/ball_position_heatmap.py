import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# CSV dosyasını yükle
csv_path = "data/output/player_positions.csv"  # Pozisyon verisi
df = pd.read_csv(csv_path)

# Top verisini filtrele
ball_positions = df[df["Player_ID"] == "Ball"]

# Saha çizimi
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw()

# Top pozisyonlarını çiz (ısı haritası)
x = ball_positions["X"] * 100
y = ball_positions["Y"] * 100
pitch.hexbin(x, y, ax=ax, gridsize=30, cmap="hot", edgecolors='none', alpha=0.7)

# Başlık ve görselleştirme
plt.title("Topun Saha Üzerindeki Yoğunluk Analizi", fontsize=16)
plt.show()
