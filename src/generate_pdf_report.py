from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

# Yazı tipini kaydet
pdfmetrics.registerFont(TTFont("DejaVu", "fonts/DejaVuSans.ttf"))

# PDF dosyasını kaydetme yolu
output_path = "reports/analysis_report.pdf"

# PDF oluşturma
c = canvas.Canvas(output_path, pagesize=A4)

# Sayfa boyutları
width, height = A4

# Başlık
c.setFont("DejaVu", 16)
c.drawCentredString(width / 2, height - 2 * cm, "Futbol Maçı Analiz Raporu")

# Yazıları daha küçük fontla yazarak sığdırma
font_size = 9
line_spacing = 0.5 * cm

# Metni bir fonksiyonla ekleme
def add_text(canvas, text_lines, start_x, start_y, font_size, line_spacing):
    canvas.setFont("DejaVu", font_size)
    y = start_y
    for line in text_lines:
        if y < 2 * cm:  # Alt marj kontrolü
            break
        canvas.drawString(start_x, y, line)
        y -= line_spacing
    return y

# Metin içerikleri
overview = [
    "Projeye Genel Bakış: Bu proje, bir futbol maçında oyuncu pozisyonlarını, pas bağlantılarını,",
    "hedefe yakınlığı ve zaman bazlı hareketleri analiz etmektedir. Sonuçlar görselleştirilerek oyuncu",
    "performansı ve takım stratejileri hakkında içgörüler sunulmuştur."
]

data_summary = [
    "1. Veri Özeti",
    "Toplam Oyuncu Sayısı: 22",
    "İşlenen Frame Sayısı: 16,050",
    "",
    "Veri Kaynakları:",
    "- Oyuncu Pozisyonları: player_positions.csv",
    "- Pas Frekansları: pass_frequencies.csv",
    "- Hedefe Yakınlık Verisi: Oyuncu Pozisyonları verilerinden türetilmiştir."
]

findings = [
    "2. Temel Bulgular",
    "2.1 Oyuncu Aktivitesi:",
    "- En Aktif Oyuncu: Player 10",
    "- Hücum ve savunma hareketlerinde yüksek katılım.",
    "- Isı Haritaları: Oyuncuların sık ziyaret ettiği alanlar belirlendi.",
    "",
    "2.2 Pas Analizi:",
    "- Pas Başarı Oranı: %84",
    "- En Sık Pas Bağlantısı: Player 7 ve Player 9 arasında.",
    "- Takım Özeti:",
    "  - A Takımı: Orta sahada baskın.",
    "  - B Takımı: Güçlü savunma pozisyonları.",
    "",
    "2.3 Hedefe Yakınlık Analizi:",
    "- Hedefe En Yakın Oyuncu: Player 9",
    "- Bulgu: Hücum bölgesinde sürekli varlık göstererek birçok gol fırsatı yarattı.",
    "",
    "2.4 Zamana Bazlı Hareket Analizi:",
    "- Belirlenen Önemli Anlar:",
    "  - İkinci yarıda artan hücum hareketleri.",
    "  - Karşı ataklarda stratejik savunma değişimleri.",
    "",
    "2.5 Gelişmiş Veri Modelleme:",
    "- Oyuncu Rolleri:",
    "  - Pozisyon ve pas verilerine göre tahmin edilen roller.",
    "  - Örnek: Player 5, defansif orta saha olarak tahmin edildi.",
    "- Makine Öğrenimi Modelleri:",
    "  - Taktiksel kalıpları belirlemek için kümeleme algoritmaları uygulandı."
]

conclusion = [
    "5. Sonuç",
    "Bu proje, futbol maçlarının analizine yenilikçi bir bakış açısı sunmaktadır.",
    "Kullanılan araçlar ve yöntemler, oyuncu performansı ve takım stratejilerinin",
    "daha iyi anlaşılmasını sağlamaktadır."
]

technologies = [
    "Kullanılan Teknolojiler:",
    "- Python" ", OpenCV" ", Mediapipe" ", mplsoccer" ", Pandas" ", Matplotlib" ", NumPy" ", Scikit-learn"
]

# Metni PDF'e ekleme
current_y = height - 3 * cm
current_y = add_text(c, overview, 2 * cm, current_y, font_size, line_spacing)
current_y -= line_spacing
current_y = add_text(c, data_summary, 2 * cm, current_y, font_size, line_spacing)
current_y -= line_spacing
current_y = add_text(c, findings, 2 * cm, current_y, font_size, line_spacing)
current_y -= line_spacing
current_y = add_text(c, conclusion, 2 * cm, current_y, font_size, line_spacing)
current_y -= line_spacing
current_y = add_text(c, technologies, 2 * cm, current_y, font_size, line_spacing)

# Sayfa numarası
c.setFont("DejaVu", 8)
c.drawString(width - 3 * cm, cm, f"Sayfa: 1")

# PDF'yi kaydet ve kapat
c.save()

print(f"PDF raporu başarıyla oluşturuldu: {output_path}")
