import shelve

berkas = open("coba1.txt", "r")
NIM = berkas.readline()
TTL = berkas.readline()
Nama = berkas.readline()
Kota = berkas.readline()

berkas = shelve.open("sop.data")
berkas["Data"] = [NIM, TTL, Nama, Kota]
berkas.close()
