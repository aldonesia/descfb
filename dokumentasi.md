#Tugas KIJ - Membuat DES dengan metode CFB

## DES
Data Encryption Standard (DES) adalah blok cipher kunci simetris yang diterbitkan oleh Institut Nasional Standar dan Teknologi (NIST). 
DES merupakan implementasi dari Feistel Cipher. Menggunakan 16 putaran struktur Feistel. Ukuran blok adalah 64-bit. Meskipun, panjang kunci adalah 64-bit, DES memiliki panjang kunci efektif 56 bit, sejak 8 dari 64 bit kunci yang tidak digunakan oleh algoritma enkripsi (berfungsi sebagai bit check saja).

## CFB mode
Dalam mode ini, setiap blok ciphertext akan 'makan kembali' ke dalam proses enkripsi untuk mengenkripsi blok plaintext berikutnya. Modus CFB berbeda secara signifikan dari mode ECB, ciphertext sesuai dengan blok plaintext diberikan tidak tergantung hanya pada blok plaintext dan kunci, tetapi juga di blok ciphertext sebelumnya. Dengan kata lain, blok ciphertext tergantung dari pesan. 