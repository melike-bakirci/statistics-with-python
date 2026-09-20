import pandas as pd

# Veri seti
data = [18, 19, 22, 23, 24, 25, 26, 27, 28, 28, 29, 30, 31, 32, 35, 38, 41, 45, 48, 52]

# Pandas Series oluşturma
s = pd.Series(data)

# İstatistiksel özet
summary = s.describe()
mode_val = s.mode().tolist()
cv = (s.std() / s.mean()) * 100

print("Veri Seti İstatistiksel Özeti:\n")
print(summary)
print(f"Mod: {mode_val}")
print(f"Değişim Katsayısı (CV): %{cv:.2f}")
