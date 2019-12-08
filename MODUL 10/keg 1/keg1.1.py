import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",30001))
s.listen(5)
print "Program komunikasi tentang data diri"
data = ""
kamus = {"nama":"Alfian Makruf Nur S",
         "NIM":"L200190184",
         "Motto":"Semua itu ada masanya",
         "alamat":"cek google maps",
         "keluar":"yes sir"}
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        print "Perintah: ", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf, perintah ini tidak diketahui")
