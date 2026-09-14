import matplotlib.pyplot as plt
import numpy as np

# Yeni senaryodaki ham veri seti (Aykırı Değerli)
teslimat_sureleri = [18, 20, 21, 22, 23, 25, 26, 27, 28, 29, 29, 31, 33, 36, 39, 41, 45, 48, 52, 110]

fig, ax = plt.subplots(figsize=(8, 6))

# ax.boxplot ile ham veriden kutu grafiği çizimi
box = ax.boxplot(teslimat_sureleri, patch_artist=True)

# Kutunun ve çizgilerin renklerini ayarlama
for patch in box['boxes']:
    patch.set_facecolor((0.1, 0.5, 0.9, 0.4))  # Mavi şeffaf dolgu
    patch.set_edgecolor('blue')

for median in box['medians']:
    median.set(color='red', linewidth=2)

for whisker in box['whiskers']:
    whisker.set(color='blue', linewidth=1.5)
    
for cap in box['caps']:
    cap.set(color='blue', linewidth=1.5)

# Aykırı değerlerin (fliers) stilini ayarlama
for flier in box['fliers']:
    flier.set(marker='o', markerfacecolor='red', markeredgecolor='red', markersize=8)

# NumPy ile verinin istatistiklerini hesaplıyoruz (Grafiğe yazdırmak için)
q1 = np.percentile(teslimat_sureleri, 25)
med = np.median(teslimat_sureleri)
q3 = np.percentile(teslimat_sureleri, 75)
iqr = q3 - q1
upper_fence = q3 + 1.5 * iqr

# Matplotlib'in hesapladığı çit içi min ve max değerler
min_val = box['caps'][0].get_ydata()[0]
max_val = box['caps'][1].get_ydata()[0]

# Değerleri grafik üzerinde minik şekilde gösterme
x_pos = 1.08 # Metinleri daha yakına alıyoruz
ax.text(x_pos, med, f"Medyan: {med}", va='center', fontsize=9, color='red')
ax.text(x_pos, q1, f"Q1: {q1}", va='center', fontsize=9, color='blue')
ax.text(x_pos, q3, f"Q3: {q3}", va='center', fontsize=9, color='blue')
ax.text(x_pos, min_val, f"Min: {min_val}", va='center', fontsize=9, color='blue')
ax.text(x_pos, max_val, f"Maks (Çit İçi): {max_val}", va='center', fontsize=9, color='blue')

# Aykırı değer (flier) için metin ekleme
fliers = box['fliers'][0].get_ydata()
for flier_val in fliers:
    ax.text(x_pos, flier_val, f"Aykırı Değer: {flier_val}", va='center', fontsize=9, color='red', fontweight='bold')

# Üst çiti temsil eden kesik çizgi ekleyelim
ax.axhline(y=upper_fence, color='orange', linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(0.55, upper_fence, f"Üst Çit ({upper_fence})", va='bottom', fontsize=9, color='orange')

# Eksen ve başlık ayarları
ax.set_ylabel('Süre (Dakika)')
ax.set_title('Aykırı Değerin (Outlier) İncelenmesi: Teslimat Süreleri Kutu Grafiği')
ax.set_xticklabels(['Kurye Teslimatları'])
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği kaydet
fig.savefig('boxplot_outlier.png')
print("Aykırı değerli kutu grafiği (boxplot_outlier.png) ham veri kullanılarak başarıyla oluşturuldu ve kaydedildi.")

