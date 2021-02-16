## Exam Modul I, 16 Feb 2021
## Kelvin Lois

# Soal 1
print("\n")
print("="*30, "Konverter Waktu", "="*30)
Input = input("Masukkan detik : ")

## Fungsi Konversi 
def timeConverter(Input):
    try:
        detik = int(Input)
        if detik < 0 or detik > 359999:
            return "Invalid input!"
        else: 
            jam = detik // 3600
            menit  = (detik - jam*3600) // 60
            detik_sisa = detik - jam*3600 - menit*60
            if jam < 10:
                j = '0'+ str(jam)
            else:
                j = str(jam)
            if menit < 10:
                m = '0'+ str(menit)
            else:
                m = str(menit)
            if detik_sisa < 10:
                d = '0'+ str(detik_sisa)
            else:
                d = str(detik_sisa)
            return f"Konversi : {j}:{m}:{d}"
    except:
        return "Invalid Input!"

print(timeConverter(Input))
    