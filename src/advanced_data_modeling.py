import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# CSV dosyasını yükle
positions_csv_path = "data/output/player_positions.csv"
df = pd.read_csv(positions_csv_path)

# Top verisini çıkar
player_positions = df[df["Player_ID"] != "Ball"]

# X ve Y pozisyonlarını normalize etmek için hazırlayın
features = player_positions[["X", "Y"]].values
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# K-Means ile kümeleme
num_clusters = 3  # Örnek olarak 3 rol
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
player_positions["Role"] = kmeans.fit_predict(features_scaled)

# Her oyuncunun en çok hangi role ait olduğunu bul
player_roles = player_positions.groupby("Player_ID")["Role"].agg(lambda x: x.value_counts().idxmax())

# Sonuçları kaydet
output_roles_csv = "data/output/player_roles.csv"
player_roles.to_csv(output_roles_csv, header=["Role"])
print(f"Player roles saved to: {output_roles_csv}")

# Küme sonuçlarını görselleştirme
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw()

# Her küme için renk ataması
colors = ['red', 'blue', 'green']
for role in range(num_clusters):
    role_positions = player_positions[player_positions["Role"] == role]
    pitch.scatter(
        role_positions["X"] * 100, role_positions["Y"] * 100,
        ax=ax, alpha=0.6, s=30, label=f"Role {role + 1}", c=colors[role]
    )

plt.title("Oyuncu Rollerinin K-Means ile Analizi", fontsize=16)
plt.legend()
output_visual_path = "data/visuals/player_roles_analysis.png"
plt.savefig(output_visual_path)
plt.show()

print(f"Role visualization saved to: {output_visual_path}")
