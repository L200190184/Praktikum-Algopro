import shelve

berkas = shelve.open("sop.data")
print("Nim:", berkas["Data"][0])
print("Tempat, Tanggal lahir:", berkas["Data"][1])
print("Nama:", berkas["Data"][2])
print("Kota:", berkas["Data"][3])
berkas.close()
