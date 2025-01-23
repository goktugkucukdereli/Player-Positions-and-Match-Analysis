from mplsoccer import Pitch
import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasının yolu
output_csv = "data/output/player_positions.csv"

# CSV dosyasını yükle
df = pd.read_csv(output_csv)

# Pozisyonları filtrele (sadece oyuncular)
player_positions = df[df['Player_ID'] != "Ball"]

# Saha çizimi
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw()

# Oyuncu pozisyonlarını çiz (normalize edilmiş X ve Y değerleri)
x = player_positions["X"] * 100  # Normalize edilmiş X değerlerini yüzdeye çevir
y = player_positions["Y"] * 100  # Normalize edilmiş Y değerlerini yüzdeye çevir
pitch.scatter(x, y, ax=ax, s=100, c="blue", edgecolor="black", alpha=0.7)

# Görselleştirme
plt.title("Oyuncu Pozisyonları Isı Haritası")
plt.show()
