def hitung_pajak(harga_barang,pajak=12):
    total_pajak = harga_barang * (pajak/100)
    total_hargabarangDanPajak = total_pajak + harga_barang
    print(f"harga barang bersama pajak adalah{ total_hargabarangDanPajak}")

hitung_pajak(1000000000000000)
