import matplotlib.pyplot as plt
import numpy as np
import math

# Teslimat sürelerini temsil eden ham veri seti (Dakika cinsinden, 20 adet)
# Diğer dosyalardaki (boxplot) aynı veri setini kullanıyoruz ki farklı grafik türleriyle farkı görelim.
teslimat_sureleri = [15, 18, 20, 21, 23, 25, 26, 26, 27, 28, 29, 30, 32, 34, 36, 38, 40, 42, 48, 52]

N = len(teslimat_sureleri)

# 1. Sınıf Sayısı (Karekök Kuralı ile)
k_raw = math.sqrt(N)
k = round(k_raw) # 4.47 -> 4 sınıfa yuvarlanır

# 2. Aralık Genişliği (Freedman-Diaconis Kuralı ile)
q1 = np.percentile(teslimat_sureleri, 25)
q3 = np.percentile(teslimat_sureleri, 75)
iqr = q3 - q1
h_raw = 2 * iqr / (N ** (1/3))
h = int(round(h_raw, -1)) # 8.84 -> 10'a yuvarlanmış birim genişliği

# 3. Sınırları oluştur (Minimum değerden başlayarak k adet sınıf için)
min_val = min(teslimat_sureleri)
sinirlar = [min_val + i * h for i in range(k + 1)]

plt.figure(figsize=(8, 6))

# plt.hist ile kendi hesapladığımız dinamik sınırları (sinirlar) kullanarak çizim yapıyoruz
plt.hist(teslimat_sureleri, bins=sinirlar, edgecolor='black', color='skyblue')

# Eksen ayarları
plt.xticks(sinirlar)
plt.yticks(range(0, 11))
plt.xlabel('Sipariş Süresi (Dakika)')
plt.ylabel('Sipariş Sayısı (Frekans)')

# Başlığı dinamik hale getiriyoruz
plt.title(f'Sipariş Süreleri Histogramı ({k} Sınıf, {h} Birim Genişlik)')

plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği kaydet
plt.savefig('histogram.png')
print(f"Histogram kendi hesapladığı sınırlarla ({k} sınıf, {h} genişlik) başarıyla oluşturuldu ve kaydedildi.")
