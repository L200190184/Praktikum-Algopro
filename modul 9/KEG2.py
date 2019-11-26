berkas = open("coba1.txt", "w")
berkas.write("L200190184\n")
berkas.write("18-08-2000\n")
berkas.write("Alfian Makruf Nur Sholehudin\n")
berkas.write("Wonogiri")
berkas.close()



berkas = open("coba1.txt", "r")
NIM = berkas.readline()
TTL = berkas.readline()
Nama = berkas.readline()
Kota = berkas.readline()


print(Nama)
print(Kota,",", TTL)
print(NIM)
berkas.close()
