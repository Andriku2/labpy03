# labspy03

Tugas Praktikum  Mata Kuliah Program Komputer dan Praktek
------------------------------------------------------------------------------------------------------------
**Algoritma Latihan1:**


Tujuan: Menentukan bilangan terbesar dari lima bilangan yang diinputkan pengguna.

Langkah-langkah Algoritma:

1.Inisialisasi dan Input Data:

Tampilkan pesan kepada pengguna untuk memasukkan lima bilangan satu per satu.

Simpan setiap bilangan yang diinputkan pengguna dalam variabel terpisah, misalnya bilangan1, bilangan2, bilangan3, bilangan4, dan bilangan5.

2.Penentuan Bilangan Terbesar:

Inisialisasi variabel terbesar dengan nilai bilangan1.
Anggap sementara bahwa bilangan1 adalah bilangan terbesar.

3.Perbandingan dengan Statement if:

Bandingkan terbesar dengan bilangan2:
Jika bilangan2 lebih besar daripada terbesar, perbarui nilai terbesar dengan bilangan2.
Bandingkan terbesar dengan bilangan3:
Jika bilangan3 lebih besar daripada terbesar, perbarui nilai terbesar dengan bilangan3.
Bandingkan terbesar dengan bilangan4:
Jika bilangan4 lebih besar daripada terbesar, perbarui nilai terbesar dengan bilangan4.
Bandingkan terbesar dengan bilangan5:
Jika bilangan5 lebih besar daripada terbesar, perbarui nilai terbesar dengan bilangan5.

4.Output Hasil:

Setelah selesai membandingkan semua bilangan, nilai dalam variabel terbesar sekarang berisi bilangan terbesar dari lima bilangan yang diinputkan.
Tampilkan nilai terbesar kepada pengguna.

**Hasil Program**

![Latihan1](https://github.com/user-attachments/assets/c31ca5e1-c60c-4f80-89c6-5e3d12759f5c)
-----------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------


**Algoritma Latihan2:**

Tujuan: Menghitung rata-rata dari beberapa bilangan yang dimasukkan oleh pengguna.

Langkah-langkah Algoritma:

1.Inisialisasi dan Input Data:

Tampilkan pesan untuk meminta pengguna memasukkan jumlah bilangan yang akan dihitung rata-ratanya.
Simpan jumlah bilangan ini dalam variabel, misalnya n.

2.Validasi Input:

Periksa apakah nilai n lebih dari nol. Jika n kurang dari atau sama dengan nol, tampilkan pesan kesalahan dan akhiri program.

Jika n valid, lanjutkan ke langkah berikutnya.

3.Input Bilangan dan Akumulasi Jumlah:

Inisialisasi variabel jumlah dengan nilai 0 untuk menyimpan penjumlahan dari semua bilangan yang diinputkan.

Gunakan perulangan (misalnya for) untuk meminta pengguna memasukkan setiap bilangan satu per satu sebanyak n kali.

Di dalam perulangan, setiap bilangan yang diinputkan ditambahkan ke variabel jumlah.

4.Perhitungan Rata-rata:

Setelah semua bilangan diinputkan, hitung rata-rata dengan membagi jumlah dengan n.

Simpan hasil rata-rata ini dalam variabel, misalnya rata_rata.

5.Output Hasil:

Tampilkan nilai rata-rata kepada pengguna.

Penjelasan Tambahan:
Program ini menggunakan perulangan untuk mengumpulkan total jumlah dari bilangan yang dimasukkan pengguna.
Dengan membagi total jumlah dengan n, kita memperoleh rata-rata.
Validasi di awal membantu memastikan bahwa program hanya melanjutkan jika jumlah bilangan (n) lebih dari nol, sehingga menghindari pembagian dengan nol.


**Hasil Program**

![Latihan2](https://github.com/user-attachments/assets/6fea8682-aea1-4859-802f-a4eb489ccebc)

--------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------

**Algoritma Program 1:**

Tujuan: Menghitung total keuntungan seorang pengusaha yang memulai usaha dengan modal awal 100 juta dan mengalami perubahan persentase keuntungan pada setiap periode tertentu selama 8 bulan.


1.Inisialisasi Modal dan Variabel Keuntungan:

Tentukan modal awal pengusaha sebesar 100 juta. Simpan nilai ini dalam variabel modal_awal.
Inisialisasi variabel keuntungan dengan nilai 0. Variabel ini digunakan untuk menampung total keuntungan selama 8 bulan.

2.Mulai Perulangan untuk Setiap Bulan (1-8):

Gunakan perulangan for dari bulan 1 hingga 8 untuk menghitung keuntungan setiap bulan sesuai dengan ketentuan berikut:
Penentuan Persentase Keuntungan Berdasarkan Bulan:

Pada bulan ke-1 dan ke-2: Tidak ada laba (keuntungan = 0).
Pada bulan ke-3 dan ke-4: Keuntungan sebesar 1% dari modal awal.
Pada bulan ke-5 hingga ke-7: Keuntungan sebesar 5% dari modal awal.
Pada bulan ke-8: Keuntungan menurun menjadi 3% dari modal awal.

3.Perhitungan Keuntungan Bulanan:

Untuk setiap bulan, hitung laba berdasarkan persentase keuntungan yang telah ditentukan.
Simpan hasil perhitungan laba bulan tersebut ke variabel laba.
Tambahkan nilai laba ke variabel keuntungan untuk mengakumulasi total keuntungan hingga bulan tersebut.

4.Output Keuntungan Bulanan (Opsional):

Selama perulangan berjalan, tampilkan keuntungan (laba) setiap bulan untuk memantau hasil perhitungan.

5.Output Total Keuntungan:

Setelah perulangan selesai (saat sudah menghitung keuntungan selama 8 bulan), tampilkan nilai dari variabel keuntungan, yang merupakan total keuntungan selama 8 bulan.

**Hasil Program**

![Program1](https://github.com/user-attachments/assets/cd40e14b-f5d0-4cd7-88f1-f6666f345e1e)

