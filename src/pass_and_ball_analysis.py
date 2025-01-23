import pandas as pd
from mplsoccer import Pitch
import matplotlib.pyplot as plt
import numpy as np

# CSV dosyasını yükle
output_csv = "data/output/player_positions.csv"
df = pd.read_csv(output_csv)

# Oyuncu pozisyonlarını ve top pozisyonlarını ayır
player_positions = df[df['Player_ID'] != "Ball"]
ball_positions = df[df['Player_ID'] == "Ball"]

# Pas bağlantılarını analiz et
def calculate_pass_connections(player_positions, threshold=0.05):
    connections = {}
    frames = player_positions['Frame'].unique()

    for frame in frames:
        frame_data = player_positions[player_positions['Frame'] == frame]
        for i, player_a in frame_data.iterrows():
            for j, player_b in frame_data.iterrows():
                if player_a['Player_ID'] != player_b['Player_ID']:
                    distance = np.sqrt(
                        (player_a['X'] - player_b['X'])**2 +
                        (player_a['Y'] - player_b['Y'])**2
                    )
                    if distance < threshold:
                        pair = tuple(sorted([player_a['Player_ID'], player_b['Player_ID']]))
                        connections[pair] = connections.get(pair, 0) + 1
    return connections

# Pas bağlantılarını hesapla
pass_connections = calculate_pass_connections(player_positions)

# Saha çizimi
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw()

# Pas bağlantılarını çiz
for connection, count in pass_connections.items():
    player_a = player_positions[player_positions['Player_ID'] == connection[0]].iloc[0]
    player_b = player_positions[player_positions['Player_ID'] == connection[1]].iloc[0]
    ax.plot(
        [player_a['X'] * 100, player_b['X'] * 100],
        [player_a['Y'] * 100, player_b['Y'] * 100],
        color='yellow', linewidth=count * 0.1, alpha=0.5
    )

# Top hareketlerini çiz
ball_x = ball_positions["X"] * 100
ball_y = ball_positions["Y"] * 100
pitch.lines(ball_x[:-1], ball_y[:-1], ball_x[1:], ball_y[1:], ax=ax, lw=2, color="red", alpha=0.7)

plt.title("Pas Bağlantıları ve Top Hareket Analizi")
plt.show()
