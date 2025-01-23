import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Pas verilerini yükle
pass_csv_path = "data/output/pass_frequencies.csv"
pass_data = pd.read_csv(pass_csv_path)

# Sütun adlarını yazdır
print("Sütun Adları:", pass_data.columns)

# Belirli bir oyuncunun pas bağlantılarını filtrele
player_id = 10  # Analiz yapılacak oyuncu ID'si
player_passes = pass_data[pass_data["From"] == player_id]  # Eğer 'From' farklıysa doğru adı yaz

# Pas bağlantılarını bir grafik olarak görselleştir
G = nx.DiGraph()

# Düğümler ve bağlantılar ekle
for _, row in player_passes.iterrows():
    G.add_edge(row["From"], row["To"], weight=row["Passes"])  # 'From', 'To', 'Passes' isimlerini kontrol et

# Grafik çizimi
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8, 6))
nx.draw(
    G, pos, with_labels=True, node_color="skyblue", edge_color="gray",
    node_size=3000, font_size=10, font_color="black", arrowsize=20
)

# Kenar ağırlıklarını göster
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title(f"Belirli Oyuncunun Pas Bağlantıları (ID: {player_id})", fontsize=16)
plt.tight_layout()

# Grafiği kaydet ve göster
plt.show()
