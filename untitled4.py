#Program mencari diskon

totalBelanja = int(input("Masukan total belanja= "))

if (totalBelanja > 2000000) :
    diskon = 0.15
elif (totalBelanja > 1000000) :
    diskon = 0.10
elif (totalBelanja > 500000) :
    diskon = 0.05
else:
        diskon = 0

print ("Selamat anda mendapat diskon", diskon*totalBelanja)