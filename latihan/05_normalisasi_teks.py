# ==========================================
# LATIHAN 05 - NORMALISASI TEKS
# Algoritma dan Pemrograman | Pertemuan 10
# ==========================================

nama = "  Siti Fitriani "

nama_bersih = " ".join(nama.strip().split())
nama_normal = nama_bersih.title()

print("Nama sebelum   :", repr(nama))
print("Nama dibersihkan:", nama_bersih)
print("Nama normal    :", nama_normal)