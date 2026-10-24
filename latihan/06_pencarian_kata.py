# ==========================================
# LATIHAN 06 - PENCARIAN KATA
# Algoritma dan Pemrograman | Pertemuan 10
# ==========================================

teks = "Saya belajar string Python"
kata = "string"

print("Teks yang dicari:", teks)
print("Kata pencarian  :", kata)

if kata in teks:
    print("Status          : Kata ditemukan")
else:
    print("Status          : Kata tidak ditemukan")

print("Posisi kata     :", teks.find(kata))