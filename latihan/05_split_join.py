# Input: Kalimat yang akan dipisahkan menjadi kata.
kalimat = "data teks perlu dibersihkan"

# Proses: Memisahkan kalimat dan menggabungkan kata dengan tanda hubung.
kata = kalimat.split()
hasil = "-".join(kata)

# Output: Menampilkan list kata dan hasil penggabungan.
print(kata)
print(hasil)
