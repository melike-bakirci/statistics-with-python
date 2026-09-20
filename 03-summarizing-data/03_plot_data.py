import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Kurye verisi
data = [18, 19, 22, 23, 24, 25, 26, 27, 28, 28, 29, 30, 31, 32, 35, 38, 41, 45, 48, 52]

s = pd.Series(data)

# Grafik oluşturma
plt.figure(figsize=(10, 6))

import numpy as np

# Histogram ve yoğunluk (KDE) grafiği (4 sınıf, 10 aralık genişliği)
bins_edges = [15, 25, 35, 45, 55]
sns.histplot(s, kde=True, bins=bins_edges, color='skyblue', edgecolor='black')

# X eksenindeki sayıları çizgi (sınıf) başlarına ve sonlarına koyma
plt.xticks(bins_edges)

# Ortalama, Medyan ve Mod çizgilerini ekleyerek sağa çarpıklığı vurgulama
mode_val = s.mode()[0]
plt.axvline(s.mean(), color='red', linestyle='dashed', linewidth=2, label=f'Ortalama: {s.mean():.2f}')
plt.axvline(s.median(), color='green', linestyle='dashed', linewidth=2, label=f'Medyan: {s.median()}')
plt.axvline(mode_val, color='orange', linestyle='dashed', linewidth=2, label=f'Mod: {mode_val}')

plt.title('Kurye Verisi Dağılımı - Sağa Çarpıklık (Right-Skewed)')
plt.xlabel('Kurye Verisi Değerleri')
plt.ylabel('Frekans')
plt.legend()
plt.grid(axis='y', alpha=0.75)

plt.tight_layout()
plt.savefig('kurye_verisi_grafik.png')
print("Grafik 'kurye_verisi_grafik.png' adıyla kaydedildi.")
