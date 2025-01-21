# Program menghitung jumlah huruf vokal
def hitung_vokal(teks):
    vokal = "aeiouAEIOU"
    jumlah = 0
    for huruf in teks:
        if huruf in vokal:
            jumlah += 1
    return jumlah

teks = input(" ")
print("Jumlah huruf vokal:", hitung_vokal(teks))
