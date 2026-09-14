import matplotlib.pyplot as plt
import numpy as np

# Teslimat sürelerini temsil eden ham veri seti (Dakika cinsinden, 20 adet)
teslimat_sureleri = [15, 18, 20, 21, 23, 25, 26, 26, 27, 28, 29, 30, 32, 34, 36, 38, 40, 42, 48, 52]

fig, ax = plt.subplots(figsize=(8, 6))

# ax.boxplot ile ham veriden kutu grafiği çizimi
# patch_artist=True kutunun içini renklendirmemizi sağlar
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

# NumPy ile verinin istatistiklerini hesaplıyoruz (Grafiğe yazdırmak için)
q1 = np.percentile(teslimat_sureleri, 25)
med = np.median(teslimat_sureleri)
q3 = np.percentile(teslimat_sureleri, 75)
min_val = min(teslimat_sureleri)
max_val = max(teslimat_sureleri)

# Değerleri grafik üzerinde minik şekilde gösterme
x_pos = 1.08 # Metinleri kutunun hemen yanına hizalıyoruz
ax.text(x_pos, med, f"Medyan: {med}", va='center', fontsize=9, color='red')
ax.text(x_pos, q1, f"Q1: {q1}", va='center', fontsize=9, color='blue')
ax.text(x_pos, q3, f"Q3: {q3}", va='center', fontsize=9, color='blue')
ax.text(x_pos, min_val, f"Min: {min_val}", va='center', fontsize=9, color='blue')
ax.text(x_pos, max_val, f"Maks: {max_val}", va='center', fontsize=9, color='blue')

# Eksen ve başlık ayarları
ax.set_ylabel('Süre (Dakika)')
ax.set_title('Operasyonun Röntgeni: Teslimat Süreleri Kutu Grafiği (Box Plot)')

# x ekseni ismini ayarlıyoruz
ax.set_xticklabels(['Kurye Teslimatları'])

ax.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği kaydet
fig.savefig('boxplot.png')
print("Kutu grafiği (boxplot.png) ham veri kullanılarak başarıyla oluşturuldu ve kaydedildi.")
