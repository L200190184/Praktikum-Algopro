## Program Akun
## Dibuat oleh Alfian Makruf Nur S 200190184
import random
angka = random.randint(0,1000)

Nama = 'Alfian Makruf Nur Sholehudin'
TanggalLahir = '18 Agustus 2000'
NamaSingkat = Nama[0] + '.' + Nama[7] + '.' + Nama[14:28]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[11:15]
Password = Nama[0:3] + str(angka)

print(Nama,TanggalLahir,NamaSingkat,Username,Password)

