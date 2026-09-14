import matplotlib.pyplot as plt

# Kategorik Veriler (3 Kategori)
kategoriler = ['Lahmacun', 'Kebap', 'Çiğ Köfte']
siparis_sayilari = [9, 7, 4]

fig, ax = plt.subplots(figsize=(8, 6))

# Bar Chart (Çubuk Grafik) oluşturma
bars = ax.bar(kategoriler, siparis_sayilari, color=['#ff9999','#66b3ff','#99ff99'])

# Y-ekseni limitini yazılar kesilmesin diye biraz yüksek tutuyoruz
ax.set_ylim(0, max(siparis_sayilari) * 1.2)

# Her çubuğun üzerine değerlerini yazdırma
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.15, int(yval), ha='center', va='bottom', fontsize=12, fontweight='bold')

# Eksen ve başlık ayarları
ax.set_xlabel('Yemek Kategorileri', fontsize=11)
ax.set_ylabel('Sipariş Sayısı', fontsize=11)
ax.set_title('Yemek Kategorilerine Göre Sipariş Dağılımı (Kategorik Veri)', fontsize=13, pad=15)

# Y-ekseni ızgarası
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği kaydet
kayit_yolu = 'barchart_categories.png'
fig.savefig(kayit_yolu)
print(f"Kategorik bar grafiği başarıyla oluşturuldu: {kayit_yolu}")
