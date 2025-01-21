def hitung_pajak(harga_barang, pajak=12):
    if harga_barang > 2000000: 
        total_pajak = harga_barang * (pajak / 100)
        total_hargabarangDanPajak = total_pajak + harga_barang
        print(f"Harga barang bersama pajak adalah {total_hargabarangDanPajak}")
    else:  
        print(f"Harga barang tidak dikenakan pajak. Totalnya tetap {harga_barang}")

hitung_pajak(200000000000000)