# Input: Teks dan kata yang ingin dicari.
teks = "Python untuk data. Python untuk pendidikan."
kata = "python"

# Proses: Menyamakan kapitalisasi dan mencari kata.
teks = teks.lower()

# Output: Menampilkan keberadaan, jumlah, dan posisi kata.
print(kata in teks)
print(teks.count(kata))
print(teks.find(kata))
