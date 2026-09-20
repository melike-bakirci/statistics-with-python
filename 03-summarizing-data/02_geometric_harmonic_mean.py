import statistics

# Geometrik Ortalama
growth_rates = [1.10, 1.20, 0.90]
geo_mean = statistics.geometric_mean(growth_rates)

print("--- Geometrik Ortalama ---")
print(f"Büyüme Çarpanları: {growth_rates}")
print(f"Geometrik Ortalama Çarpanı: {geo_mean:.4f}")
print(f"Ortalama Yıllık Büyüme Oranı: %{(geo_mean - 1) * 100:.2f}\n")

# Harmonik Ortalama
speeds = [120, 60]
harm_mean = statistics.harmonic_mean(speeds)

print("--- Harmonik Ortalama ---")
print(f"Hızlar: {speeds}")
print(f"Harmonik Ortalama: {harm_mean:.2f}")
