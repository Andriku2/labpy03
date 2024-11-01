# Modal awal pengusaha
modal_awal = 100000000  # 100 juta
keuntungan = 0  # Inisialisasi total keuntungan

# Menghitung keuntungan per bulan
for bulan in range(1, 9):  # 1 sampai 8 (8 bulan)
    if bulan == 3 or bulan == 4:
        laba = modal_awal * 0.01  # 1% keuntungan
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba = modal_awal * 0.05  # 5% keuntungan
    elif bulan == 8:
        laba = modal_awal * 0.03  # 3% keuntungan
    else:
        laba = 0  # Bulan pertama dan kedua belum ada laba

    keuntungan += laba  # Menambah keuntungan bulan ini ke total

    # Menampilkan laba setiap bulan
    print(f"Bulan ke-{bulan}: Laba = {laba}")

# Menampilkan total keuntungan selama 8 bulan
print(f"\nTotal keuntungan selama 8 bulan = {keuntungan}")
