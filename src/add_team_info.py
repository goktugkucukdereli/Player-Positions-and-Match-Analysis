import pandas as pd
import numpy as np

# CSV dosyasını yükle
positions_csv_path = "data/output/player_positions.csv"
df = pd.read_csv(positions_csv_path)

# Oyunculara rastgele takım atama
unique_players = df["Player_ID"].unique()
team_assignments = {player: np.random.choice(["Team A", "Team B"]) for player in unique_players}
df["Team_ID"] = df["Player_ID"].map(team_assignments)

# Yeni CSV dosyasına kaydet
output_csv_path = "data/output/player_positions_with_teams.csv"
df.to_csv(output_csv_path, index=False)

print(f"Takım bilgileri eklendi ve kaydedildi: {output_csv_path}")
