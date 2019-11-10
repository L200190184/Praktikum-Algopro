Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama='Alfian Makruf Nur Sholehudin'
>>> NIM='L200190184'
>>> X='1' + NIM[7:]
>>> a=int(X)
>>> b=len(Nama)
>>> type(a)
<class 'int'>
>>> # variabel a merupakan data tipe integer karena telah diubah  dari data tipe
>>> type(b)
<class 'int'>
>>> # variabel b merupakan data tipe integer karena data tersebut mengandung intruksi len yang mana len adalah jumlah anggota dari suatu objek
>>> a / b
42.285714285714285
>>> # merupakan data yang bertipe float karena 1184 dibagi 28 menghasilkan bilangan float 42.285714285714285 atau mengandung nilai desimal
>>> a//b
42
>>> # merupakan data yang bertipe integer karena hasil bagi dari 1184 dibagi 28 yang hasilnya 42.285714285714285 dibulat kan kebawah menjadi 42 yang bertipe integer, karena data bertipe integer dibagi data bertipe integer maka menghasilkan data bertipe integer pula
>>> 10 * (a - 999)
1850
>>> # merupakan data yang bertipe integer , karena data dari variabel a dikurang 999 adalah 185 dan kemudian dikalikan dengan 10 menghasilkan data 1850
>>> b ** 2
784
>>> # merupakan data yang bertipe integer , karena data dari variabel b pangkat kan 2 atau 28 pangkat 2 yang menghasilkan data 784
>>> a % b
8
>>> #merupakan data yang bertipe integer , karena simbol % merupakan sisa hasil bagi dari data variabel a dibagi data variabel b atau sisa hasil bagi dari 1184 dibagi 28 yaitu 8
>>> c = 12.5
>>> # data 12.5 disimpan dalam variabel c
>>> type(c)
<class 'float'>
>>> # variabel c merupakan data float karena mengandung nilai desimal
>>> a / c
94.72
>>> # merupakan data bertipe float karena data variabel a dibagi dengan data variabel c sama dengan 94.72 atau 1184 dibagi 12.5 menghasilkan data 94.72 yang bertipe float atau bernilai desimal
>>> a // c
94.0
>>> # merupakan data yang bertipe float karena dalam variabel c mengandung data bertipe float maka hasil pembagian dibulatkan kebawah dari variabel data bertipe integer dibagi variabel data bertipe float adalah data bertipe float 1184 dibagi 12.5 dan dibulatkan ke bawah menghasilkan data 94.0
>>> a % c
9.0
>>> # merupakan data yang bertipe float karena sisa hasil bagi(%) antara data variabel a(1184) dengan data variabel c(12.5) menghasilkan 9.0 yang mengandung nilai desimal
>>> c > b
False
>>> # merupakan data yang bertipe boolean yang bernilai atau berkondisi False karena data variabel c (12.5) lebih kecil dari data variabel b (28) sedangkan dalam program ditulis data variabel c lebih besar dari pada data variabel b maka menghasilkan kondisi atau nilai False
>>> type(c > b)
<class 'bool'>
>>>  # merupakan data yang bertipe boolean yang memiliki 2 kondisi atau nilai yaitu True dan False , merupakan operator logika
 
>>> a > b and b > c
True
>>> # merupakan data yang bertipe boolean yang berkondisi atau bernilai True karena a > b bernilai True dan b > c bernilai True juga , dalam operator 'and' apabila kedua data memiliki nilai True maka menghasilkan data bernilai True
>>> a > 1100 or b < 10
True
>>> # merupakan data yang bertipe boolean yang berkondisi atau bernilai True karena a > 1100 bernilai True dan b < 10 bernilai False , dalam operator 'or' apabila salah satu memiliki nilai True maka menghasilkan data bernilai True juga
