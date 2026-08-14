# mengambil input dari pengguna
harga_beli = float(input("Masukkan harga beli saham (Rp): "))
harga_jual = float(input("Masukkan harga jual saham (Rp): "))
jumlah_lembar = int(input("Masukkan jumlah lembar saham: "))

# melakukan perhitungan matematika dasar
total_modal = harga_beli * jumlah_lembar
total_pendapatan = harga_jual * jumlah_lembar
keuntungan_nominal = total_pendapatan - total_modal

# menghitung persentase keuntungan
persentase_keuntungan = (keuntungan_nominal / total_modal) * 100

# menampilkan hasil perhitungan
print("\nHasil Perhitungan:")
print(f"Total Modal: Rp {total_modal:,.2f}")
print(f"Total Pendapatan: Rp {total_pendapatan:,.2f}")
print(f"Keuntungan Nominal: Rp {keuntungan_nominal:,.2f}")
print(f"Persentase Keuntungan: {persentase_keuntungan:.2f}%")

# logika keputusan sederhana (if/else)
if keuntungan_nominal > 0:
    print("Status: Profit(untung)🎉")
elif keuntungan_nominal < 0:
    print("Status: Loss(rugi)😢")
else:
    print("Status: Impas (break-even)😐")