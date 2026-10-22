# Input: Nama lengkap mahasiswa dan kode kelas.

# Proses 1: Membersihkan dan menormalkan nama.
def normalisasi_nama(nama):
    return nama.strip().title()


# Proses 2: Membuat inisial dari setiap kata nama.
def buat_inisial(nama):
    kata = nama.split()
    inisial = ""

    for x in kata:
        inisial += x[0].upper()

    return inisial


# Proses 3: Menormalkan kode kelas menjadi huruf besar
# dan mengganti spasi dengan tanda hubung.
def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    return "-".join(kata)


# Input: Membaca nama dan kode kelas dari pengguna.
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Proses: Menormalisasi data dan menghitung jumlah kata.
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama_bersih)

# Output: Menampilkan hasil normalisasi.
print("\n=== HASIL NORMALISASI DATA MAHASISWA ===")
print(f"Nama bersih  : {nama_bersih}")
print(f"Kode kelas   : {kode_bersih}")
print(f"Jumlah kata  : {jumlah_kata}")
print(f"Inisial      : {inisial}")
