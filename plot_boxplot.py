import matplotlib.pyplot as plt

# Metinde belirtilen değerler
# Medyan (Q2): 28.5
# Alt Çeyreklik (Q1): 24.5
# Üst Çeyreklik (Q3): 36.5
# Çeyrekler Arası Açıklık (IQR): 12

# Kutu grafiği istatistiklerini doğrudan tanımlıyoruz ki metinle birebir uyumlu olsun
stats = [{
    'label': '',
    'med': 28.5,
    'q1': 24.5,
    'q3': 36.5,
    'whislo': 15,  # Örnek minimum değer
    'whishi': 52,  # Örnek maksimum değer
    'fliers': []
}]

fig, ax = plt.subplots(figsize=(8, 6))

# bxp ile önceden hesaplanmış istatistiklerle kutu grafiği çizimi
# Kutu içi dolu ve mavi şeffaf yapıldı (RGBA: (0, 0, 1, 0.3))
ax.bxp(stats, patch_artist=True, 
        boxprops=dict(facecolor=(0.1, 0.5, 0.9, 0.4), color='blue'),
        whiskerprops=dict(color='blue'),
        capprops=dict(color='blue'),
        medianprops=dict(color='red', linewidth=2))

# Değerleri grafik üzerinde minik şekilde gösterme
x_pos = 1.08 # Metinleri daha yakına (kutunun hemen yanına) alıyoruz
ax.text(x_pos, stats[0]['med'], f"Medyan: {stats[0]['med']}", va='center', fontsize=9, color='red')
ax.text(x_pos, stats[0]['q1'], f"Q1: {stats[0]['q1']}", va='center', fontsize=9, color='blue')
ax.text(x_pos, stats[0]['q3'], f"Q3: {stats[0]['q3']}", va='center', fontsize=9, color='blue')
ax.text(x_pos, stats[0]['whislo'], f"Min: {stats[0]['whislo']}", va='center', fontsize=9, color='blue')
ax.text(x_pos, stats[0]['whishi'], f"Maks: {stats[0]['whishi']}", va='center', fontsize=9, color='blue')

# Eksen ve başlık ayarları
ax.set_ylabel('Süre (Dakika)')
ax.set_title('Operasyonun Röntgeni: Teslimat Süreleri Kutu Grafiği (Box Plot)')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği kaydet
fig.savefig('c:\\Users\\melik\\Desktop\\veri\\boxplot.png')
print("Kutu grafiği (boxplot.png) başarıyla oluşturuldu ve kaydedildi.")
