#Daftar harga barang 
harga_barang = {
    "Pulpen": 5000,
    "Pensil": 3000,
    "Buku Tulis":20000,
    "Penghapus":2500,
    "Penggaris":7000
    
}
def diskon():
    if total_belanja > 2500000:
        return total_belanja * 0.25
        
    elif total_belanja > 100000:
        return total_belanja * 0.10
    
    elif total_belanja > 500000:
         return total_belanja * 0.05
    
    else:
        return 0
        
                
total_belanja = 0
while True:
    nama_barang = input("Masukkan nama barang:")
    if nama_barang not in harga_barang:
        print("Barang anda tidak ada, silakan masukkan barang kembali")
        continue
    
    jumlah = int(input("masukkan jumlah barang"))
    total_belanja += harga_barang[nama_barang]*jumlah
    
    verif = input("Mau belanja lagi? ketik belanja/selesai")
    if verif == "selesai":
        break
    
    if barang.lower() == "selesai":
        break
    print(harga_barang)
    if barang in harga_barang:
        jumlah = int(input(f"Masukkan jumlah {barang}:"))
        total_belanja += harga_barang[barang] * jumlah
    else:
        print("Barang tidak tersedia.Silakan masukkan barang yang benar.")
    

    
jumlah_potongan = total_belanja * diskon 
total_bayar = total_belanja - potongan



