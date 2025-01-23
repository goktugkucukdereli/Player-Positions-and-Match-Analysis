from mplsoccer import Pitch
import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını yükle
csv_path = "data/output/player_positions.csv"
df = pd.read_csv(csv_path)

# Player_ID türünü kontrol et ve gerektiğinde dönüştür
if df["Player_ID"].dtype == "object":
    df["Player_ID"] = pd.to_numeric(df["Player_ID"], errors="coerce")

# Oyuncuların ID'sini seç
player_id = 10  # Örnek olarak ID 10 olan oyuncuyu seçiyoruz

# Mevcut oyuncu ID'lerini kontrol et
print("Mevcut oyuncular:", df["Player_ID"].unique())

# Belirli bir oyuncunun pozisyonlarını filtrele
player_data = df[(df["Player_ID"] == player_id)]

# Eğer oyuncuya ait veri yoksa, uyarı mesajı ver
if player_data.empty:
    print(f"Player_ID == {player_id} için kayıt bulunamadı.")
else:
    # Eksik pozisyon verilerini kontrol et
    missing_positions = player_data[player_data[["X", "Y"]].isnull().any(axis=1)]
    if not missing_positions.empty:
        print(f"Player_ID == {player_id} için {len(missing_positions)} eksik kayıt bulundu:")
        print(missing_positions)
    
    # Eksik kayıtları çıkar
    player_data = player_data.dropna(subset=["X", "Y"])

    # Saha çizimi
    pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
    fig, ax = pitch.draw()

    # Oyuncunun pozisyonlarını ısı haritası olarak çiz
    x = player_data["X"] * 100
    y = player_data["Y"] * 100
    pitch.kdeplot(x, y, ax=ax, cmap="Reds", fill=True, levels=100, alpha=0.7)
    plt.title(f"Oyuncu {player_id} İçin Saha Üzerindeki Hareket Yoğunluğu", fontsize=16)

    # Görseli kaydet ve göster
    plt.show()
