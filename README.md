
# Pertemuan 10 - String dan Pengolahan Teks

Nama: Maulyditha Revania A.
NIM: 2225250100
Kelas: 3A

## Tujuan
Mengolah dan menormalisasi data teks menggunakan string Python.

## Struktur Program
Folder latihan berisi enam program:
1. 01_dasar_string.py: Operasi dasar string.
2. 02_indeks_slicing.py: Mengakses karakter dan slicing.
3. 03_method_string.py: Menggunakan method string.
4. 04_membersihkan_teks.py: Membersihkan spasi berlebih.
5. 05_split_join.py: Memisahkan dan menggabungkan kata.
6. 06_pencarian_kata.py: Mencari kata dalam teks.

Folder tugas berisi:
- normalisasi_data_mahasiswa.py: Menormalisasi nama dan kode kelas.

## Cara Menjalankan
Jalankan dari folder utama repositori:

python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_membersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py
python tugas/normalisasi_data_mahasiswa.py

## Algoritma
1. Membaca nama dan kode kelas.
2. Menghapus spasi di awal dan akhir nama.
3. Mengubah nama menjadi title case.
4. Memisahkan nama menjadi beberapa kata.
5. Membentuk inisial dari huruf pertama setiap kata.
6. Mengubah kode kelas menjadi huruf besar.
7. Menggabungkan bagian kode dengan tanda hubung.
8. Menampilkan hasil normalisasi.

## Test Case
| Input nama | Input kode | Hasil |
|---|---|---|
| aan hendrayana | pmat a 2026 | Aan Hendrayana, PMAT-A-2026, AH |
| fATHIYYAH mUTHMAINNAH | kelas b | Fathiyyah Muthmainnah, KELAS-B, FM |
| BUDI | pmtk 01 | Budi, PMTK-01, B |
| siti nur aisyah | kelas c | Siti Nur Aisyah, KELAS-C, SNA |

Isi hasil aktual dan status berdasarkan pengujian yang benar-benar dilakukan.

## Refleksi
Saya memahami bahwa string memiliki method untuk
membersihkan spasi, mengubah kapitalisasi, memisahkan
kata, dan menggabungkan teks. Saya juga belajar menggunakan
fungsi agar proses normalisasi dapat digunakan kembali.

Salah satu masalah yang saya pelajari adalah spasi berlebih
dalam teks. Masalah ini dapat diperbaiki menggunakan strip(),
split(), dan join().
