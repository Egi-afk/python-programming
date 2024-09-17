jumlah_karyawan = int(input("masukkan jumlah karyawan"))

for i in range (jumlah_karyawan):
    print (f"Karyawan ke{i+1}")
    nama_karyawan = input("Masukkan nama karyawan: ")
    jam_kerja = int(input("masukkan jam kerja"))

    tarif_normal = 50000
    tarif_lembur = 75000

    if jam_kerja > 40:
        jam_lembur = jam_kerja - 40
        gaji = (40 * tarif_normal) + (jam_lembur * tarif_lembur)
    else:
        gaji = jam_kerja * tarif_normal
    
    print(f"nama karyawan {nama_karyawan} mendapatkan gaji pokok sebesar {gaji}")
