import pandas as pd
import numpy as np

# CSV dosyasını yükle
positions_csv_path = "data/output/player_positions.csv"
output_pass_csv_path = "data/output/pass_frequencies.csv"
df = pd.read_csv(positions_csv_path)

# "Ball" verisini filtrele ve sadece oyuncuları al
player_positions = df[df["Player_ID"] != "Ball"].copy()

# Boş değerleri kontrol et ve temizle
player_positions.dropna(inplace=True)

# Pas bağlantılarını simüle etmek için bir DataFrame oluştur
pass_data = []

# Frame bazında oyuncuları grupla
grouped_frames = player_positions.groupby("Frame")

for frame, group in grouped_frames:
    players = group["Player_ID"].unique()
    for i, from_player in enumerate(players):
        for j, to_player in enumerate(players):
            if i != j:  # Kendisine pas olmaz
                # Her oyuncu çifti için bir ağırlık oluştur
                weight = np.random.randint(1, 5)  # Örnek olarak rastgele bir ağırlık
                pass_data.append({"From": from_player, "To": to_player, "Passes": weight})

# Veriyi DataFrame'e çevir ve kaydet
pass_df = pd.DataFrame(pass_data)
pass_df = pass_df.groupby(["From", "To"]).sum().reset_index()  # Aynı oyuncu çifti için pasları topla
pass_df.to_csv(output_pass_csv_path, index=False)

print(f"Pass frequencies saved to: {output_pass_csv_path}")
