import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter

# CSV dosyalarını yükle
positions_csv_path = "data/output/player_positions.csv"  # Pozisyon verisi

# Oyuncu pozisyonları analizini yap
df_positions = pd.read_csv(positions_csv_path)
player_positions = df_positions[df_positions["Player_ID"] != "Ball"]

# En aktif oyuncuları (pozisyon bazında) analiz et
top_active_players = player_positions["Player_ID"].value_counts().head(10)

# En aktif oyuncuların bar grafiği (pozisyon bazlı)
plt.figure(figsize=(10, 6))
top_active_players.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("En Aktif Oyuncular (Pozisyon Bazında)", fontsize=16)
plt.xlabel("Oyuncu ID", fontsize=12)
plt.ylabel("Aktivite Sayısı", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Grafiği kaydet ve göster
plt.show()

# CSV dosyasını yükle
positions_csv_path = "data/output/player_positions.csv"  # Pozisyon verisi
df_positions = pd.read_csv(positions_csv_path)

# "Ball" verisini filtrele ve sadece oyuncuları al
player_positions = df_positions[df_positions["Player_ID"] != "Ball"]

# Oyuncuları karelere göre gruplandır
frames = player_positions.groupby("Frame")

# Pas bağlantılarını simüle et (aynı karede yakın oyuncular arasında)
pass_connections = []
for frame, group in frames:
    player_coords = group[["Player_ID", "X", "Y"]].values
    for p1, p2 in combinations(player_coords, 2):
        # Oyuncuların ID'leri ve pozisyonları
        id1, x1, y1 = p1
        id2, x2, y2 = p2
        # İki oyuncu arasındaki mesafeyi hesapla (örnek: yakınlık kriteri < 0.05)
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if distance < 0.05:  # Yakınlık kriteri
            pass_connections.append((int(id1), int(id2)))

# Pas bağlantılarını say
pass_freq = Counter(pass_connections)
pass_df = pd.DataFrame(
    [(from_player, to_player, count) for (from_player, to_player), count in pass_freq.items()],
    columns=["From", "To", "Passes"]
)

# En aktif oyuncuları hesapla
outgoing_passes = pass_df.groupby("From")["Passes"].sum().reset_index(name="Outgoing Passes")
incoming_passes = pass_df.groupby("To")["Passes"].sum().reset_index(name="Incoming Passes")
player_activity = pd.merge(outgoing_passes, incoming_passes, left_on="From", right_on="To", how="outer").fillna(0)
player_activity["Player_ID"] = player_activity["From"].combine_first(player_activity["To"])
player_activity = player_activity[["Player_ID", "Outgoing Passes", "Incoming Passes"]]

# En aktif oyuncuları görselleştir
player_activity["Total Passes"] = player_activity["Outgoing Passes"] + player_activity["Incoming Passes"]
player_activity = player_activity.sort_values(by="Total Passes", ascending=False)

# Bar grafiği oluştur
plt.figure(figsize=(12, 6))
plt.bar(player_activity["Player_ID"].astype(int), player_activity["Total Passes"], color="skyblue", edgecolor="black")
plt.title("En Aktif Oyuncular (Simüle Edilmiş Pas Verisi)", fontsize=16)
plt.xlabel("Oyuncu ID", fontsize=12)
plt.ylabel("Toplam Pas Sayısı", fontsize=12)
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Grafiği kaydet ve göster
plt.show()