import matplotlib.pyplot as plt

# Sınıf orta noktaları (x ekseni için)
x = [20, 30, 40, 50]
# Frekanslar (y ekseni için)
frequencies = [5, 9, 3, 3]
# Sınıf sınırları
bins = [15, 25, 35, 45, 55]

plt.figure(figsize=(8, 6))
# Histogram çizimi (çubuk genişliği 10, kenarlar belirgin)
plt.bar(x, frequencies, width=10, edgecolor='black', color='skyblue', align='center')

# Eksen ayarları
plt.xticks(bins)
plt.yticks(range(0, 11))
plt.xlabel('Sipariş Süresi (Dakika)')
plt.ylabel('Sipariş Sayısı (Frekans)')
plt.title('Sipariş Süreleri Histogramı (4 Sınıf, 10 Birim Genişlik)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği kaydet
plt.savefig('histogram.png')
print("Histogram başarıyla oluşturuldu ve kaydedildi.")
