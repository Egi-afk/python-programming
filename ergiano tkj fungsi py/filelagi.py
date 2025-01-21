def cek_nilai(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    else:
        return "D"
        
grade = int(input("Masukkan nilai anda:"))
grade_result = cek_nilai(grade)


