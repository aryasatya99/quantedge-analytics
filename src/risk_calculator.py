import math
#Data historis return harian saham (%) selama 5 hari terakhir
returns = [0.02, -0.01, 0.03, -0.02, 0.01]

# Menghitung rata-rata return (mean)
total_return = sum(returns)
jumlah_hari = len(returns)
rata_rata_return = total_return / jumlah_hari

# menghitung Varians (jarak kuadrat tiap data ke return rata-rata)
selisih_kuadrat = []
for r in returns:
    kuadrat = (r - rata_rata_return) ** 2
    selisih_kuadrat.append(kuadrat)

    varians = sum(selisih_kuadrat) / jumlah_hari

    # Menghitung standar deviasi (akar kuadrat dari varians)
    standar_deviasi = math.sqrt(varians)

    # menapilkan hasil perhitungan
    print("===analisis risiko saham===")
    print(f"Rata-rata Return: {rata_rata_return:.4f}")
    print(f"Varians: {varians:.6f}")
    print(f"Standar Deviasi: {standar_deviasi:.4f}")

    # logika penentuan tingkat risiko
    if standar_deviasi < 0.01:
        tingkat_risiko = "Rendah"
    elif standar_deviasi < 0.02:
        tingkat_risiko = "Sedang"
    else:
        tingkat_risiko = "Tinggi"
    print(f"Tingkat Risiko: {tingkat_risiko}")