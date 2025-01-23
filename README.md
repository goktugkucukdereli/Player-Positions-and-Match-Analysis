# Oyuncu Pozisyonları ve Maç Analizi

## 🎯 Proje Amacı

Bu proje, futbol maçlarının oyuncu hareketlerini, pas bağlantılarını, top hareketlerini ve stratejilerini analiz ederek bu verileri görselleştirme ve video analizleriyle sunmak için geliştirilmiştir.
Oyuncu pozisyonları, pas bağlantıları ve hedefe yakınlık analizleri gibi metrikler üreten proje, futbol analitiği ve scouting süreçlerini desteklemekte, oyuncu performansını değerlendirme ve stratejik kararlar için yenilikçi çözümler sunmaktadır.

## 📌 Proje Hedefleri

**Oyuncu Performansı Analizi:
- Oyuncuların saha içindeki hareketlerini ve performanslarını detaylı olarak analiz etmek.

**Pas Bağlantıları ve Top Hareketi:
- Pas bağlantılarını ve topun saha üzerindeki hareketini görselleştirerek oyun içi stratejilerin anlaşılmasını kolaylaştırmak.

**Takım Bazlı Analizler:
- Takımların saha içindeki etkinliklerini karşılaştırmalı olarak analiz etmek.

**Zaman Bazlı Analizler:
- Oyuncu ve top hareketlerini zaman içinde inceleyerek oyun içindeki dinamikleri anlamak.

**Hedefe Yakınlık Analizi:
- Oyuncuların ve topun kaleye olan mesafelerini analiz ederek etkili pozisyonları tespit etmek.

**Video Analizi Entegrasyonu:
- Analiz sonuçlarını maç videolarıyla senkronize ederek görsel olarak sunmak.

**Gelişmiş Veri Modelleme:
- Makine öğrenmesi algoritmaları kullanarak oyuncu rollerini ve stratejik oyun kalıplarını belirlemek.

---

## 📈 Proje Sonuçları

1. **Dinamik Pozisyon Analizi**
   - Videodan oyuncuların pozisyonları tespit edilerek bir CSV dosyasına kaydedildi.
   - Oyuncuların hareket yoğunlukları bir futbol sahası üzerinde görselleştirildi.

2. **Pas ve Top Hareket Analizi**
   - Oyuncuların pas bağlantıları simüle edilerek en çok pas yapan oyuncular belirlendi.
   - Topun sahadaki hareket yoğunluğu ve belirli bölgelerdeki hareketleri analiz edildi.

3. **Takım Bazlı Analizler**
   - Oyuncular takımlara ayrıldı ve her takımın saha içindeki hareket yoğunlukları ve pas örüntüleri incelendi.

4. **Zaman Bazlı Hareket Analizi**
   - Oyuncuların ve topun belirli zaman dilimlerindeki pozisyonları analiz edildi.
   - Hareketlerin oyun içindeki zamanlaması ile etkileri incelendi.

5. **Hedefe Yakınlık Analizi**
   - Oyuncuların ve topun kaleye olan uzaklığı zaman içinde takip edilerek görselleştirildi.

6. **Gelişmiş Veri Modelleme**
   - Veri madenciliği ve kümeleme teknikleri kullanılarak oyuncuların rolü ve stratejik davranışları belirlendi.

7. **Video Analizi ile Entegrasyon**
   - Analiz edilen veriler bir futbol videosu üzerine yerleştirildi.
   - Oyuncu pozisyonları ve önemli anlar görsel olarak video üzerinde vurgulandı.

---

## 📋 Projenin İçeriği

### 1. Oyuncu Pozisyonları Isı Haritası
- Oyuncuların saha üzerindeki hareketlerini ısı haritası şeklinde görselleştirir.

### 2. Pas ve Top Hareket Analizi
- Oyuncular arasındaki pas bağlantılarını ve topun saha üzerindeki hareketini analiz eder.

### 3. Takım Bazlı Analizler
- İki takımın saha içindeki etkinliklerini kıyaslar.

### 4. Zaman Bazlı Hareket Analizi
- Oyuncuların ve topun zaman içindeki hareketlerini inceleyerek oyun dinamiklerini anlamaya yardımcı olur.

### 5. Hedefe Yakınlık Analizi
- Oyuncuların ve topun kaleye olan yakınlıklarını analiz ederek etkili pozisyonları tespit eder.

### 6. Gelişmiş Veri Modelleme
- Veri madenciliği ve makine öğrenmesi yöntemleriyle oyuncu rolleri ve oyun kalıplarını belirler.

### 7. Video Analizi ile Entegrasyon
- Analiz verilerini maç videolarıyla entegre ederek görsel bir sunum sağlar.

---

## 🛠️ Kullanılan Teknolojiler ve Araçlar

| **Teknolojiler Araçlar**              | **Kullanım Amacı**                                     |
|---------------------------------------|--------------------------------------------------------|
| Python                                | Veri işleme ve analiz için temel programlama dili.     |
| OpenCV                                | Video işleme ve çıktı videoları oluşturma.             |
| Mediapipe                             | Oyuncu ve top pozisyonlarının tespiti.                 |
| mplsoccer                             | Futbol sahası görselleştirme ve analiz grafikleri      |
| NetworkX                              | Pas ağlarının görselleştirilmesi.                      |
| Pandas                                | Veri manipülasyonu ve CSV dosyalarını işleme.          |
| Matplotlib                            | Görselleştirme.                                        |
| NumPy                                 | Profesyonel veri görselleştirme.                       |
| Scikit-learn                          | Makine öğrenmesi ve gelişmiş veri analizi.             |
| itertools (combinations)              | Oyuncu bağlantılarını analiz için kullanıldı.          |
| collections (Counter)                 | Frekans hesaplamaları için kullanıldı.                 |
| Tableau                               | Profesyonel veri görselleştirme.                       |

---

## 🚀 Projenin Çalıştırılması

### Gereksinimler
- Python 3.8+
- Gerekli Python kütüphaneleri (pandas, matplotlib, seaborn, scikit-learn, imbalanced-learn, networkx)

## Kurulum

1. Bu projeyi yerel makinenize klonlayın:
   ```bash
   git clone https://github.com/goktugkucukdereli/Futbol-Scouting-ve-Performans-Analizi.git
   ```

2. Sanal bir ortam oluşturun ve gerekli kütüphaneleri yükleyin:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Gerekli kütüphaneleri yüklemek için:
    ```bash
    pip install -r requirements.txt
    ```

4. Her bir analiz için ilgili Python dosyasını çalıştırın. Örneğin:
   ```bash
   python src/player_10_heatmap.py
   ```
   Bu analiz, seçilen bir oyuncunun saha üzerindeki hareket yoğunluğunu gösterir.

---

## 📊 Görselleştirmeler ve Analizler

### Oyuncu Pozisyonları Isı Haritası
Oyuncuların saha üzerindeki hareketlerinin yoğunluk dağılımını gösterir.

![Player Positions Heatmap](reports/visuals/player_positions_heatmap.png)

---

### Pas ve Top Hareket Analizi
Oyuncular arasındaki pas bağlantılarını ve topun saha üzerindeki hareketlerini analiz eder.

![Pass and Ball Movement Analysis](reports/visuals/pass&ball_analysis.png)

---

### Takım Bazlı Analizler

**Takım A Isı Haritası:**
Takım A oyuncularının saha üzerindeki hareket yoğunluğunu gösterir.

![Team A Heatmap](reports/visuals/team_a_heatmap.png)

---

**Takım Aktivite Karşılaştırması:**
İki takımın saha içindeki etkinliklerini kıyaslar.

![Team Activity Comparison](reports/visuals/team_activity_comparison.png)

---

### Zaman Bazlı Hareket Analizi
Zaman içinde oyuncu ve top hareketlerini analiz ederek oyun dinamiklerini görselleştirir.

![Time-Based Movement Analysis](reports/visuals/time_based_movement_analysis.gif)

---

### Hedefe Yakınlık Analizi
Oyuncuların ve topun kaleye olan mesafelerini analiz eder.

![Proximity to Goal Analysis](reports/visuals/proximity_to_goal_analysis.png)

---

### Gelişmiş Veri Modelleme
Makine öğrenmesi yöntemleriyle oyuncu rolleri ve stratejik oyun kalıplarını belirler.

![Player Roles Analysis](reports/visuals/player_roles_analysis.png)

---

### Oyuncu Pas Analizi
Belirli bir oyuncunun pas bağlantılarını ve hangi oyuncularla daha sık paslaştığını analiz eder.

![Player Pass Analysis](reports/visuals/player_pass_analysis.png)

---

### En Aktif Oyuncular (Simüle Edilmiş Pas Verisi)
Simüle edilmiş pas verisine dayanarak en aktif oyuncuları belirler.

![Player Activity by Simulated Passes Analysis](reports/visuals/player_activity_by_simulated_passes_analysis.png)

---

### En Aktif Oyuncular (Pozisyon Bazında)
Oyuncuların pozisyon verilerine dayanarak saha üzerinde en aktif olanları analiz eder.

![Player Activity by Position Analysis](reports/visuals/player_activity_by_position.png)

---

### Oyuncu 10 İçin Saha Üzerindeki Hareket Yoğunluğu
Oyuncu 10'un saha üzerindeki hareket yoğunluğunu görselleştirir.

![Player 10 Heatmap Analysis](reports/visuals/player_10_heatmap.png)

---

### Oyuncular Arasındaki Pas Bağlantı Ağı
Oyuncular arasındaki pas bağlantılarını ağırlıklarla birlikte görselleştirir.

![Pass Network Analysis](reports/visuals/pass_network_analysis.png)

---

### Topa En Yakın Oyuncular
Topa en yakın oyuncuları ve bu yakınlıkların zaman içindeki değişimini analiz eder.

![Closest Players to Ball Analysis](reports/visuals/closest_players_to_ball.png)

---

### Topun Saha Üzerindeki Yoğunluk Analizi
Topun saha üzerindeki yoğunluk dağılımını analiz eder.

![Ball Position Heatmap Analysis](reports/visuals/ball_position_heatmap.png)

---

### Video Analizi ile Entegrasyon
Analiz sonuçlarını maç videolarıyla senkronize ederek görsel bir sunum sağlar.

![Video Analysis Integration](reports/visuals/video_analysis.gif)

---

## 📂 Proje Yapısı

```plaintext
oyuncu_pozisyonları_ve_maç_analizi/
│
├── data/
│   ├── frames/
│   │   ├── frame_0.jpg
│   │   └── ..
│   │
│   ├── output/
│   │   ├── pass_frequencies.csv
│   │   ├── player_positions_with_teams.csv
│   │   ├── player_positions.csv
│   │   └── player_roles.csv
│   │
│   └── videos/
│       ├── argentina-france_final.mp4
│       └── output_with_analysis.mp4
│
├── fonts/
│   └── DejaVuSans.ttf
│
├── notebooks/
│   └── analysis.ipynb
│
├── reports/
│   └── visuals/
│   │   ├── ball_positions_heatmap.png
│   │   └── ..
│   │
│   ├── analysis_report.pdf
│   └── summary.txt
│
├── src/
│   ├── add_team_info.py
│   └── ..
│
├── venv/
│   └── ..
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 📜 Lisans
Projeyi MIT Lisansı ile lisansladım. Lisans detayları için LICENSE dosyasını inceleyebilirsiniz.
