import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Daftar Ticker Saham Big-Cap
ticker_symbols = ["BBCA.JK", "BBRI.JK", "BMRI.JK", "TLKM.JK", "ASII.JK"]
print(f"Mengunduh data saham untuk analisis tingkat lanjut: {ticker_symbols}...")

# Mengambil data harga penutupan 1 tahun terakhir
data_harga = yf.download(ticker_symbols, period="1y")['Close']

# 2. Menhitung Return Harian
returns = data_harga.pct_change().dropna()

# 3. Menghitung Sharpe Ratio (Annualized)
risk_free_rate = 0.06 # BI Rate ~6%
annualized_return = returns.mean() * 252
annualized_volatility = returns.std() * np.sqrt(252)
sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility

analisis_sharpe = pd.DataFrame({
    'Annualized Return (%)': annualized_return * 100,
    'Annualized Volatility (%)': annualized_volatility * 100,
    'Sharpe Ratio': sharpe_ratio
})

print("\n=== HASIL ANALISIS SHARPE RATIO (1 TAHUN) ===")
print(analisis_sharpe.round(2).sort_values(by='Sharpe Ratio', ascending=False))

# 4. Matriks Korelasi
korelasi = returns.corr()
print("\n=== MATRIKS KORELASI ANTAR-SAHAM ===")
print(korelasi.round(2))

# 5. Visualisasi Heatmap Korelasi
plt.figure(figsize=(8, 6))
plt.imshow(korelasi, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(label='Tingkat Korelasi')

for i in range(len(ticker_symbols)):
    for j in range(len(ticker_symbols)):
        plt.text(j, i, f"{korelasi.iloc[i, j]:.2f}", 
                 ha="center", va="center", color="black" if abs(korelasi.iloc[i, j]) < 0.7 else "white")

plt.xticks(range(len(ticker_symbols)), ticker_symbols, rotation=45)
plt.yticks(range(len(ticker_symbols)), ticker_symbols)
plt.title("Matriks Korelasi Portofolio Saham (Heatmap)")
plt.tight_layout()
plt.show()