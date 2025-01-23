import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# CSV dosyasını yükle
df = pd.read_csv("data/output/player_positions.csv")

# Oyuncu pozisyonlarını filtrele
player_positions = df[df['Player_ID'] != "Ball"]

# Pas bağlantılarını belirlemek için oyuncuların X ve Y pozisyonlarına göre en yakın komşularını buluyoruz
pass_links = []
player_positions = player_positions.sort_values(by="Frame")

for frame in player_positions["Frame"].unique():
    frame_data = player_positions[player_positions["Frame"] == frame]
    frame_coords = frame_data[["Player_ID", "X", "Y"]].values
    
    for i, player1 in enumerate(frame_coords):
        for j, player2 in enumerate(frame_coords):
            if i != j:  # Kendisine pas veremez
                distance = ((player1[1] - player2[1]) ** 2 + (player1[2] - player2[2]) ** 2) ** 0.5
                if distance < 0.05:  # Belirli bir mesafe içinde olanları pas bağlantısı olarak kabul ediyoruz
                    pass_links.append((player1[0], player2[0]))

# Pas bağlantı frekanslarını hesapla
pass_freq = pd.DataFrame(pass_links, columns=["From", "To"])
pass_freq = pass_freq.groupby(["From", "To"]).size().reset_index(name="Passes")

# NetworkX kullanarak pas ağı oluştur
G = nx.DiGraph()
for _, row in pass_freq.iterrows():
    G.add_edge(row["From"], row["To"], weight=row["Passes"])

# Ağ grafiğini görselleştir
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=500, node_color="lightblue")
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color="gray", width=1)
nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")

# Kenar ağırlıklarını göster
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Oyuncular Arasındaki Pas Bağlantı Ağı", fontsize=14)
plt.show()
