
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)
    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

lulus = nilai_lulus(nilai)
belum_lulus = len(nilai) - len(lulus)

print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Seluruh nilai  : {nilai}")
print(f"Banyak data    : {len(nilai)}")
print(f"Total nilai    : {sum(nilai)}")
print(f"Rata-rata      : {rata_rata(nilai):.2f}")
print(f"Nilai minimum  : {min(nilai)}")
print(f"Nilai maksimum : {max(nilai)}")
print(f"Nilai lulus    : {lulus}")
print(f"Jumlah lulus   : {len(lulus)}")
print(f"Belum lulus    : {belum_lulus}")

print("\n=== PENGUJIAN TEST CASE ===")

print("Rata-rata:", rata_rata([60, 70, 80]))
print("Minimum:", min([60, 70, 80]))
print("Maksimum:", max([60, 70, 80]))
print("Jumlah lulus:", len(nilai_lulus([59, 60, 61])))
print("Rata-rata data kosong:", rata_rata([]))