#Program Konversi Detik Ke Jam

tdetik = int(input("Masukan nilai dalam detik= "))
jam = tdetik//3600
sisa = jam % 3600
menit = sisa//60
sisa = menit % 60
detik = sisa %60

print ("Nilai setelah dikonversi adalah ", jam, "jam", menit, "menit", detik,"detik")
