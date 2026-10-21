# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Aulia Rahma Ramadhani  
**NIM:** 2225250001  
**Kelas:** 3A

## Tujuan

1. Memahami penggunaan list untuk menyimpan kumpulan data numerik.
2. Mengolah data menggunakan fungsi `len()`, `sum()`, `min()`, dan `max()`.
3. Menghitung rata-rata nilai menggunakan fungsi.
4. Memisahkan nilai lulus dan belum lulus berdasarkan batas nilai 60.
5. Menguji program menggunakan beberapa test case.
6. Menggunakan Git dan GitHub untuk menyimpan serta mendokumentasikan hasil pekerjaan.

## Struktur Program

```text
pertemuan-09-list-2225250001/
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
├── kuis/
│   └── kuis2_deret_aritmetika.py
├── praktik/
│   └── analisis_nilai_mahasiswa.py
└── README.md
```

Keterangan:

- `latihan/`: berisi latihan penggunaan list dan pengolahan data.
- `kuis/`: berisi program kuis deret aritmetika.
- `praktik/analisis_nilai_mahasiswa.py`: program untuk menganalisis nilai mahasiswa, menghitung statistik nilai, serta menentukan jumlah nilai lulus dan belum lulus.
- `README.md`: dokumentasi tujuan, struktur program, cara menjalankan, hasil pengujian, dan refleksi.

## Cara Menjalankan

Pastikan Python sudah terpasang di komputer dan terminal berada di folder utama repository `pertemuan-09-list-2225250001`.

### A. Menjalankan Program Latihan

Jalankan setiap file latihan menggunakan perintah berikut:

**1. Membuat List**

```bash
python latihan/01_buat_list.py
```

**2. Indeks dan Slicing**

```bash
python latihan/02_indeks_slicing.py
```

**3. Manipulasi List**

```bash
python latihan/03_manipulasi_list.py
```

**4. Agregasi Nilai**

```bash
python latihan/04_agregasi_nilai.py
```

**5. Filter Kelulusan**

```bash
python latihan/05_filter_kelulusan.py
```

**6. Fungsi Statistik**

```bash
python latihan/06_fungsi_statistik.py
```

### B. Menjalankan Program Praktik

Jalankan program analisis nilai mahasiswa menggunakan perintah berikut:

```bash
python praktik/analisis_nilai_mahasiswa.py
```
Program akan menampilkan seluruh nilai mahasiswa, jumlah data, total nilai, rata-rata, nilai minimum dan maksimum, daftar nilai lulus, jumlah mahasiswa lulus, serta jumlah mahasiswa yang belum lulus.

### C. Menjalankan Pengujian Test Case

Pengujian test case untuk fungsi statistik dan kelulusan juga dapat dijalankan melalui program praktik di atas. Hasil pengujian akan ditampilkan pada bagian `PENGUJIAN TEST CASE`.

## Hasil Program

Data nilai yang digunakan:

```python
[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
```

Hasil keluaran program:

```text
=== ANALISIS NILAI MAHASISWA ===
Seluruh nilai  : [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
Banyak data    : 10
Total nilai    : 695
Rata-rata      : 69.50
Nilai minimum  : 45
Nilai maksimum : 90
Nilai lulus    : [78, 90, 67, 60, 82, 71, 88]
Jumlah lulus   : 7
Belum lulus    : 3
```

## Test Case

| No. | Data uji | Aspek yang diuji | Hasil yang diharapkan | Hasil aktual | Status |
|---:|---|---|---|---|---|
| 1 | Data utama (10 nilai) | Banyak data | 10 | 10 | Berhasil |
| 2 | Data utama (10 nilai) | Total nilai | 695 | 695 | Berhasil |
| 3 | Data utama (10 nilai) | Rata-rata | 69.50 | 69.50 | Berhasil |
| 4 | Data utama (10 nilai) | Minimum dan maksimum | 45 dan 90 | 45 dan 90 | Berhasil |
| 5 | Data utama (10 nilai) | Daftar nilai lulus | `[78, 90, 67, 60, 82, 71, 88]` | `[78, 90, 67, 60, 82, 71, 88]` | Berhasil |
| 6 | Data utama (10 nilai) | Jumlah lulus dan belum lulus | 7 dan 3 | 7 dan 3 | Berhasil |
| 7 | `[60, 70, 80]` | Rata-rata | 70.00 | Belum diuji | Perlu diuji |
| 8 | `[60, 70, 80]` | Minimum dan maksimum | 60 dan 80 | Belum diuji | Perlu diuji |
| 9 | `[60, 70, 80]` | Jumlah nilai lulus | 3 | Belum diuji | Perlu diuji |
| 10 | `[59, 60, 61]` | Batas kelulusan 60 | 2 nilai lulus | Belum diuji | Perlu diuji |
| 11 | `[]` | Rata-rata list kosong | Tidak error | Belum diuji | Perlu diuji |

**Catatan:** Hasil aktual pada nomor 1–6 berdasarkan program yang sudah dijalankan. Untuk nomor 7–11, jalankan pengujian terlebih dahulu, kemudian ganti keterangan hasil aktual dan status sesuai keluaran terminal.

## Refleksi

1. Saya memahami bahwa list dapat digunakan untuk menyimpan banyak data dalam satu variabel. Setiap elemen list memiliki indeks yang dimulai dari 0. List juga dapat diolah menggunakan fungsi seperti `len()`, `sum()`, `min()`, dan `max()`.

2. Saya belajar menggunakan fungsi untuk menghitung rata-rata dan memisahkan nilai yang memenuhi batas kelulusan. Saya juga memahami pentingnya menangani list kosong agar fungsi rata-rata tidak mengalami kesalahan pembagian dengan nol.

## Kesimpulan

Program analisis nilai mahasiswa menggunakan list dan fungsi Python untuk menghitung jumlah data, total, rata-rata, nilai minimum, nilai maksimum, serta mengelompokkan nilai lulus dan belum lulus dengan batas kelulusan 60.
