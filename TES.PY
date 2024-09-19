harga_anak = 30000
harga_dewasa = 50000
harga_lansia = 35000

jumlah_pembeli = int(input("masukkan jumlah pembeli tiket: "))

total_harga = 0

for i in range(jumlah_pembeli):
    print(F"\nPembeli ke-{i+1}")
    umur = int(input("masukkan umur: "))
    jumlah_tiket = int(input("masukkan jumlah tiket yang dibeli: "))

    if umur < 12:
        harga_tiket = harga_anak
    elif 12 <= umur < 60:
        harga_tiket = harga_dewasa
    else:
        harga_tiket = harga_lansia

    harga_total_pembeli = harga_tiket * jumlah_tiket 
    total_harga += harga_total_pembeli
        
    print(f"Harga tiket untuk pembeli ini : Rp.{harga_total_pembeli}")

    print(f"\nTotal harga selururh tiket:  Rp.{total_harga}")
    


