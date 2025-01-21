#buat fungsi untuk cek sebuah diskon dan menampilkan total yang harus dibayar
def cek_diskon(total_belanja):
    batas_diskon = 1000000
    persen_diskon = 0,3
    
    if total_belanja >= batas_diskon:
        potongan = (persen_diskon / 100) * total_belanja
        total_bayar = total_belanja - potongan
        return f"Total belanja:
         Rp{total_belanja}, potongan:
          Rp{int(potongan)}, total bayar:
         Rp{int(total_bayar)}"
    else:
        return f"Total belanja:
    Rp{total_belanja}, Tidak ada diskon"