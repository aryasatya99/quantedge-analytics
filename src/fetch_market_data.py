import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Daftar Ticker Saham (Big Caps)
ticker_symbols = ["BBCA.JK", "BBRI.JK", "BMRI.JK", "TLKM.JK", "ASII.JK"]
print(f"Mengunduh data saham {ticker_symbols} dari Yahoo Finance...")

# Mengambil harga penutupan (Close) 1 bulan terakhir
data_harga = yf.download(ticker_symbols, period="1mo")['Close']

# 2. Menampilkan 5 data harian terakhir
print("\n=== 5 DATA HARIAN TERAKHIR (HARGA CLOSE) ===")
print(data_harga.tail())

# 3. Menghitung Return Harian & Volatilitas untuk Masing-Masing Saham
data_return = data_harga.pct_change()

# Menghitung Rata-rata Return & Volatilitas (Std Dev) per saham
ringkasan_analisis = pd.DataFrame({
    'Rata-Rata Return (%)': data_return.mean() * 100,
    'Volatilitas / Risk (%)': data_return.std() * 100
})

print("\n=== HASIL ANALISIS PORTOFOLIO ===")
print(ringkasan_analisis.round(2))

# 4. Membuat Visualisasi Grafik
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Grafik 1: Pertumbuhan Harga Dinormalisasi (Base 100)
# Semua saham dimulai dari angka 100 agar perbandingannya adil
data_normal = (data_harga / data_harga.iloc[0]) * 100

for ticker in ticker_symbols:
    ax1.plot(data_normal[ticker], label=ticker)

ax1.set_title('Perbandingan Performa Pergerakan Saham (Base 100)')
ax1.set_ylabel('Pertumbuhan (%)')
ax1.grid(True)
ax1.legend()

# Grafik 2: Risk vs Return Bar Chart
ringkasan_analisis.plot(kind='bar', ax=ax2)
ax2.set_title('Perbandingan Rata-Rata Return & Volatilitas (Risiko)')
ax2.set_ylabel('Persentase (%)')
ax2.set_xticklabels(ticker_symbols, rotation=0)
ax2.grid(True)

plt.tight_layout()
print("\nMenampilkan grafik...")
plt.show()