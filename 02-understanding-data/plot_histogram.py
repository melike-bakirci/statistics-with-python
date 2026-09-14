import matplotlib.pyplot as plt

# Teslimat sürelerini temsil eden ham veri seti (Dakika cinsinden, 20 adet)
# Diğer dosyalardaki (boxplot) aynı veri setini kullanıyoruz ki farklı grafik türleriyle farkı görelim.
teslimat_sureleri = [15, 18, 20, 21, 23, 25, 26, 26, 27, 28, 29, 30, 32, 34, 36, 38, 40, 42, 48, 52]

# Sınıf sınırları (bins)
sinirlar = [15, 25, 35, 45, 55]

plt.figure(figsize=(8, 6))

# plt.hist ile ham veriden histogram çizimi
# bins parametresi sınırları belirler, matplotlib frekansları kendisi sayar
plt.hist(teslimat_sureleri, bins=sinirlar, edgecolor='black', color='skyblue')

# Eksen ayarları
plt.xticks(sinirlar)
plt.yticks(range(0, 11))
plt.xlabel('Sipariş Süresi (Dakika)')
plt.ylabel('Sipariş Sayısı (Frekans)')
plt.title('Sipariş Süreleri Histogramı (4 Sınıf, 10 Birim Genişlik)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği kaydet
plt.savefig('histogram.png')
print("Histogram ham veri kullanılarak başarıyla oluşturuldu ve kaydedildi.")
