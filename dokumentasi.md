# Tugas KIJ - Membuat DES dengan metode CFB

## DES
Data Encryption Standard (DES) adalah blok cipher kunci simetris yang diterbitkan oleh Institut Nasional Standar dan Teknologi (NIST). 
DES merupakan implementasi dari Feistel Cipher. Menggunakan 16 putaran struktur Feistel. Ukuran blok adalah 64-bit. Meskipun, panjang kunci adalah 64-bit, DES memiliki panjang kunci efektif 56 bit, sejak 8 dari 64 bit kunci yang tidak digunakan oleh algoritma enkripsi (berfungsi sebagai bit check saja).

## CFB mode
Dalam mode ini, setiap blok ciphertext akan 'makan kembali' ke dalam proses enkripsi untuk mengenkripsi blok plaintext berikutnya. Modus CFB berbeda secara signifikan dari mode ECB, ciphertext sesuai dengan blok plaintext diberikan tidak tergantung hanya pada blok plaintext dan kunci, tetapi juga di blok ciphertext sebelumnya. Dengan kata lain, blok ciphertext tergantung dari pesan. 

## Langkah langkah DES dengan CFB ( run file des_cfb.py )
Langkah-langkah:
  1.	Langkah pertama
    a.	Ubah plaintext kedalam biner
    b.	Ubah key kedalam biner
    c.  Ubah iv kedalam biner
  2.	Langkah kedua: Lakukan Initial Permutation (IP) pada bit plaintext menggunakan tabel IP
  3.	Langkah ketiga: Generate kunci yang akan digunakanuntuk mengenkripsi plaintext dengan menggunakan tabel permutasi kompresi PC-1,         pada langkah ini terjadi kompresi dengan membuang 1 bit masing-masing blok kunci dari 64 bit menjadi 56 bit
  4.	Langkah keempat: Lakukan pergeseran kiri (Left Shift)
  5.	Langkah kelima: Pada langkah ini, kita akan meng-ekspansi data Ri-1 32 bit menjadi Ri 48 bit sebanyak 16 kali putaran dengan nilai       perputaran 1<= i <=16 menggunakan Tabel Ekspansi (E)
  6.	Langkah keenam: Setiap Vektor Ai disubstitusikan kedelapan buah S-Box(Substitution Box), dimana blok pertama disubstitusikan
      dengan S1, blok kedua dengan S2 dan seterusnya dan menghasilkan output vektor Bi32 bit.
  7.  iv xor dengan C[i]D[i]

## Des CFB menerapatkan socket client server (menggunakan des_server.py dan des_client.py)
  1. samakan host dan port sesuai server (ifconfig)
  2. menggunakan socket, sehingga client dapat mengirimkan data berupa pilihan(encrypt/decrypt), key, iv dan text yang akan di encrypt / 
     bilangan hex yang akan di decrypt
  3. server dapat mengirimkan hasil encrypt atau decrypt ke client, proses encrypt maupun decrypt hanya terjadi di server.

## Membuat key dengan metode Diffie-Hellman
  1. Permisalan, client adalah alice dan server adalah bob
  2. misal inputan alice adalah xa dan inputan bob = xb
  3. dengan persetujuan q=353 dan a=3
  4. menghitung respective public key dengan cara
      untuk key alice -> ya = a**xa mod q
      untuk key bob   -> yb = 3**xb mod q
  5. menghitung shared session key
      untuk key alice -> Kab = yb**xa mod q
      untuk key bob   -> kab = ya**xb mod q
  6. bila kab alice dan kab bob sama maka akan dijadikan key untuk proses encrypt dan decrypt selanjutnya
 
## Membuat key dengan RSA
  1. untuk di client masukkan bilangan prima yang pertama dan kedua
  2. di server akan menghitung public key dan private key
  3. di server masukkan nilai q
  4. server akan mengencrypt q menggunakan RSA
  5. di client akan decrypt q menggunakan RSA
  6. lalu di server masukkan a
  7. di server jg akan decrypt a menggunakan RSA
  8. di client akan encrypt a menggunakan RSA
  9. selanjutnya mengikuti langkah Diffie-hellman
## Referensi
  http://octarapribadi.blogspot.co.id/2012/10/contoh-enkripsi-dengan-algoritma-des.html
  untuk referensi socket menggunakan tugas dari mata kuliah pemrograman jaringan Pak Hudan Studiawan di Semester 5 Teknik Informatika ITS.
  untuk referensi diffie-hellman menggunakan materi dari mata kuliah Keamanan informasi dan jaringan Pak Tohari Ahmad di Semester 6 Teknik Informatika ITS.
  untuk referensi RSA menggunakan github dari https://gist.github.com/JonCooperWorks/5314103
## Dibuat oleh :
   Rizky Fenaldo Maulana  - 5114100040
   Glleen Allan M         - 5114100171
