# Tugas KIJ - Membuat DES dengan metode CFB

## DES
Data Encryption Standard (DES) adalah blok cipher kunci simetris yang diterbitkan oleh Institut Nasional Standar dan Teknologi (NIST). 
DES merupakan implementasi dari Feistel Cipher. Menggunakan 16 putaran struktur Feistel. Ukuran blok adalah 64-bit. Meskipun, panjang kunci adalah 64-bit, DES memiliki panjang kunci efektif 56 bit, sejak 8 dari 64 bit kunci yang tidak digunakan oleh algoritma enkripsi (berfungsi sebagai bit check saja).

## CFB mode
Dalam mode ini, setiap blok ciphertext akan 'makan kembali' ke dalam proses enkripsi untuk mengenkripsi blok plaintext berikutnya. Modus CFB berbeda secara signifikan dari mode ECB, ciphertext sesuai dengan blok plaintext diberikan tidak tergantung hanya pada blok plaintext dan kunci, tetapi juga di blok ciphertext sebelumnya. Dengan kata lain, blok ciphertext tergantung dari pesan. 

## Langkah langkah DES dengan CFB
Langkah-langkah:
  1.	Langkah pertama
    a.	Ubah plaintext kedalam biner
    b.	Ubah key kedalam biner
  2.	Langkah kedua: Lakukan Initial Permutation (IP) pada bit plaintext menggunakan tabel IP
  3.	Langkah ketiga: Generate kunci yang akan digunakanuntuk mengenkripsi plaintext dengan menggunakan tabel permutasi kompresi PC-1,         pada langkah ini terjadi kompresi dengan membuang 1 bit masing-masing blok kunci dari 64 bit menjadi 56 bit
  4.	Langkah keempat: Lakukan pergeseran kiri (Left Shift)
  5.	Langkah kelima: Pada langkah ini, kita akan meng-ekspansi data Ri-1 32 bit menjadi Ri 48 bit sebanyak 16 kali putaran dengan nilai       perputaran 1<= i <=16 menggunakan Tabel Ekspansi (E)
  6.	Langkah keenam: Setiap Vektor Ai disubstitusikan kedelapan buah S-Box(Substitution Box), dimana blok pertama disubstitusikan dengan       S1, blok kedua dengan S2 dan seterusnya dan menghasilkan output vektor Bi32 bit.


## Referensi
  http://octarapribadi.blogspot.co.id/2012/10/contoh-enkripsi-dengan-algoritma-des.html
  


## Dibuat oleh :
   Rizky Fenaldo Maulana  - 5114100040
   Gllen Allan Marchelim  - 5114100171
