def operasi(angka, fungsi):
    return fungsi(angka)

hasil = operasi(5, lambda x: x * 23)
print(hasil)


def tambah(number1,number2):
    return number1 + number2

def kali(number1,number2):
    return number1 * number2

def bagi(number1,number2):
    return number1 / number2

def operasi(number1,number2,fungsi):
    return fungsi(number1,number2)

HasilTambah = operasi(10,10,tambah)
print("hasil dari pertambahan = ",HasilTambah)

#Fungsi ini untuk menghitung tambah,kali,bagi
#Parameter:number(int)
#output:hasil penjumlahan kali,tambah,bagi
