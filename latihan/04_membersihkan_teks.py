# Input: Kalimat dengan spasi di awal dan akhir.
teks = " belajar python untuk pendidikan "

# Proses: Menghapus spasi tepi dan merapikan spasi berulang.
teks = teks.strip()
while "  " in teks:
    teks = teks.replace("  ", " ")

# Output: Menampilkan kalimat dengan huruf awal kapital.
print(teks.capitalize())
