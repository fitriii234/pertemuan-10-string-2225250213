
# Program Analisis Nilai Mahasiswa

print("=== ANALISIS NILAI MAHASISWA ===")

nama = input("Masukkan nama mahasiswa: ")
jumlah_nilai = int(input("Masukkan jumlah nilai: "))

nilai_list = []

for i in range(jumlah_nilai):
    nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
    nilai_list.append(nilai)

# Menghitung statistik nilai
total = sum(nilai_list)
rata_rata = total / jumlah_nilai
nilai_tertinggi = max(nilai_list)
nilai_terendah = min(nilai_list)

# Menentukan predikat
if rata_rata >= 85:
    predikat = "A"
elif rata_rata >= 75:
    predikat = "B"
elif rata_rata >= 65:
    predikat = "C"
elif rata_rata >= 50:
    predikat = "D"
else:
    predikat = "E"

# Menentukan kelulusan
if rata_rata >= 60:
    status = "Lulus"
else:
    status = "Tidak Lulus"

# Menampilkan hasil analisis
print("\n=== HASIL ANALISIS NILAI ===")
print("Nama Mahasiswa :", nama)
print("Daftar Nilai   :", nilai_list)
print("Total Nilai    :", total)
print("Rata-rata      :", round(rata_rata, 2))
print("Nilai Tertinggi:", nilai_tertinggi)
print("Nilai Terendah :", nilai_terendah)
print("Predikat       :", predikat)
print("Status         :", status)
