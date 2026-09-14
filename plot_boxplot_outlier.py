import matplotlib.pyplot as plt

# Yeni senaryodaki değerler (Aykırı Değerli)
# Q1: 24.5
# Medyan (Q2): 29
# Q3: 39.5
# Üst çit (Upper Fence): 62
# Aykırı Değer: 110
# Çit içindeki normal max değer (whishi): 52
# Çit içindeki normal min değer (whislo): 18

stats = [{
    'label': '',
    'med': 29,
    'q1': 24.5,
    'q3': 39.5,
    'whislo': 18,
    'whishi': 52,
    'fliers': [110] # Aykırı değerler listesi
}]

fig, ax = plt.subplots(figsize=(8, 6))

# Kutu içi dolu ve mavi şeffaf yapıldı (RGBA: (0, 0, 1, 0.3))
ax.bxp(stats, patch_artist=True, 
        boxprops=dict(facecolor=(0.1, 0.5, 0.9, 0.4), color='blue'),
        whiskerprops=dict(color='blue'),
        capprops=dict(color='blue'),
        medianprops=dict(color='red', linewidth=2),
        flierprops=dict(marker='o', markerfacecolor='red', markeredgecolor='red', markersize=8))

# Değerleri grafik üzerinde minik şekilde gösterme
x_pos = 1.08 # Metinleri daha yakına alıyoruz
ax.text(x_pos, stats[0]['med'], f"Medyan: {stats[0]['med']}", va='center', fontsize=9, color='red')
ax.text(x_pos, stats[0]['q1'], f"Q1: {stats[0]['q1']}", va='center', fontsize=9, color='blue')
ax.text(x_pos, stats[0]['q3'], f"Q3: {stats[0]['q3']}", va='center', fontsize=9, color='blue')
ax.text(x_pos, stats[0]['whislo'], f"Min: {stats[0]['whislo']}", va='center', fontsize=9, color='blue')
ax.text(x_pos, stats[0]['whishi'], f"Maks (Çit İçi): {stats[0]['whishi']}", va='center', fontsize=9, color='blue')

# Aykırı değer (flier) için metin ekleme
ax.text(x_pos, stats[0]['fliers'][0], f"Aykırı Değer: {stats[0]['fliers'][0]}", va='center', fontsize=9, color='red', fontweight='bold')

# Üst çiti temsil eden temsili bir kesik çizgi ekleyelim
upper_fence = 62
ax.axhline(y=upper_fence, color='orange', linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(0.55, upper_fence, f"Üst Çit (62)", va='bottom', fontsize=9, color='orange')

# Eksen ve başlık ayarları
ax.set_ylabel('Süre (Dakika)')
ax.set_title('Aykırı Değerin (Outlier) İncelenmesi: Teslimat Süreleri Kutu Grafiği')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği kaydet
fig.savefig('c:\\Users\\melik\\Desktop\\veri\\boxplot_outlier.png')
print("Aykırı değerli kutu grafiği (boxplot_outlier.png) başarıyla oluşturuldu ve kaydedildi.")
