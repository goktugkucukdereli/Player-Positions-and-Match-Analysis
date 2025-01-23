import pandas as pd
from mplsoccer import Pitch
import matplotlib.pyplot as plt

# Takım bilgisi eklenmiş CSV dosyasını yükle
positions_csv_path = "data/output/player_positions_with_teams.csv"
df = pd.read_csv(positions_csv_path)

# Takım bazlı hareket yoğunluğu
teams = df["Team_ID"].unique()

for team in teams:
    team_data = df[df["Team_ID"] == team]
    x = team_data["X"] * 100
    y = team_data["Y"] * 100

    # Saha çizimi
    pitch = Pitch(pitch_type="statsbomb", pitch_color="grass", line_color="white")
    fig, ax = pitch.draw()
    pitch.kdeplot(x, y, ax=ax, cmap="coolwarm", fill=True, levels=100, alpha=0.7)

    plt.title(f"{team} Takımı Hareket Yoğunluğu", fontsize=16)
    output_path = f"data/visuals/{team}_heatmap.png"
    plt.savefig(output_path)
    print(f"Heatmap kaydedildi: {output_path}")
    plt.show()

# Toplam pas sayısı ve başarı oranı karşılaştırması
team_passes = df.groupby("Team_ID").size()
team_passes.plot(kind="bar", color=["blue", "red"], edgecolor="black")
plt.title("Takımların Toplam Aktivitesi", fontsize=16)
plt.xlabel("Takım", fontsize=12)
plt.ylabel("Aktivite Sayısı", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
output_path = "data/visuals/team_activity_comparison.png"
plt.savefig(output_path)
print(f"Takım bazlı karşılaştırma grafiği kaydedildi: {output_path}")
plt.show()
