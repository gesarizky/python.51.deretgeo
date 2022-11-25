# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com


# Menginput
a = int(input("Masukan Nilai Awal Deret : "))
r = int(input("Masukan Nilai Rasio Deret : "))
n = int(input("Masukan Nilai Deret : "))

# Mengkonversi
un = pow(r,(n-1)) * a
sn = a * (pow(r,n)-1)/(r-1)


# Menampilkan Hasil
print('==========================================================')
print('Maka Nilai Suku Ke ',n,'=',un)
print('Maka Nilai Penjumlahan Deret =',sn)
print('==========================================================')
