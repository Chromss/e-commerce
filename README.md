- Nama: Nabil Zahid Rahman
- NPM: 2306203324
- Kelas: PBP-A

## Jawaban Soal Nomor 1
### Initialisasi Proyek Django
1. Membuat proyek Django baru dimulai dengan membuat direktori yang menyimpan berkas proyek dan membuat virtual environment di dalamnya.
2. Melakukan instalasi dependensi pada ```requirements.txt```, pembatasan konten Git pada ```.gitignore```, dan inisiasi app itu sendiri yang mengandung urls, wsgi, dsb.
### Initialisasi Aplikasi Main
3. Membuat aplikasi main dalam framework Django yang antarfile nya kemudian dikaitkan.
4. Mengkonfigurasi host yang diizinkan dan app yang terinstall pada file settings di dalam ```e_commerce```.
### Routing Pada Proyek
5. Menghubungkan file views untuk menampilkan konten yang di-assign pada variable.
6. Menghubungkan urls pada main dan urls pada e_commerce agar dapat menampilkan konten di main.
7. Menghubungkan models pada main untuk mendaftarkan atribut pada konten main ke depannya, yakni nama, harga, dan deskripsi.
### Modelling Pada Aplikasi Main
8. Membuat class Product yang meng-inherit models.Model untuk mendaftarkan atribut nama, harga, dan deskripsi
9. Menginitialisasi atribut dari class tergantung Field-nya. Misal: Nama dalam CharField, Price dalam IntegerField, dan Description dalam TextField.
### Fungsi ```views.py``` yang Menghubungkan Pada Template HTML
10. Menginisiasi 3 properti, yakni nama aplikasi (app), nama lengkap (name), dan kelas (class) dengan isian yang sesuai.
11. Me-return value dari ketiga properti tersebut pada ```main.html```, yakni ditulis dengan {{ app }}, {{ name }}, dan {{ class }}.
### Routing urls.py yang Menghubungkan ```views.py```
12. Meng-import method show_main pada ```views.py``` ke ```urls.py``` agar dapat di-return di main.
### Deployment ke PWS
13. Membuat sebuah proyek PWS baru dengan path berupa nama aplikasi (HomifyInc).
14. Menghubungkan PWS dengan git lokal dengan menambahkan remote.
15. Melakukan add, commit, dan push ke GitHub dan PWS untuk menjalankan ```main.html``` yang telah dibuat.

## Jawaban Soal Nomor 2
Alur: Client -> ```urls.py``` -> ```views.py``` -> ```models.py``` -> HTML PAGE
1. Ketika seorang klien mengirimkan permintaan HTTP ke aplikasi Django, langkah pertama yang dilakukan Django adalah memeriksa file urls.py untuk menemukan URL yang sesuai dengan permintaan tersebut dan menentukan view mana yang akan menangani prosesnya.
2. Setelah URL ditemukan dan dipetakan ke view tertentu, Django memanggil fungsi view tersebut. Di dalam fungsi view, biasanya terdapat logika untuk mengolah data, yang seringkali diambil dari database melalui model yang sudah didefinisikan dalam file ```models.py```.
3. Jika view membutuhkan data dari database, fungsi ini akan berkomunikasi dengan model untuk mengambil atau menyimpan informasi yang relevan.
4. Setelah semua data diproses di view, hasil akhirnya dikirim ke template untuk dirender menjadi halaman HTML yang lengkap, yang kemudian dikirimkan kembali ke klien sebagai respons atas permintaan mereka.

## Jawaban Soal Nomor 3
Git adalah sistem kontrol yang memungkinkan pengembang perangkat lunak untuk bekerja secara kolaboratif terkait proyek penulisan kode. Dengan Git, setiap perubahan yang dilakukan pada kode dapat dicatat dalam repositori, memudahkan untuk kembali ke versi sebelumnya jika diperlukan. Fitur cabang dan penggabungan (branching dan merging) memungkinkan pengembang untuk mengerjakan fitur baru atau perbaikan tanpa mempengaruhi kode utama secara langsung. Selain itu, Git juga memfasilitasi kolaborasi tim dengan memungkinkan beberapa pengembang untuk bekerja pada proyek yang sama secara bersamaan sehingga pembagian kerja dapat diatur secara efektif.

## Jawaban Soal Nomor 4
Django sering dipilih sebagai framework awal untuk pembelajaran pengembangan perangkat lunak karena kemudahan penggunaannya dan dokumentasinya yang lengkap sehingga memudahkan pemula memahami konsep dasar pemrograman berbasis web. Framework ini menyediakan banyak fitur bawaan, seperti sistem autentikasi dan admin panel, menjadikan pengembang untuk dapat memulai proyek tanpa membuat semuanya dari nol. Selain itu, Django mengikuti prinsip "DRY" (Don't Repeat Yourself) yang mendorong praktik pemrograman yang efisien dan terstruktur. Django juga memperhatikan keamanan proyek yang dibuat dengan menawarkan perlindungan terhadap berbagai ancaman umum dalam pengembangan web.

## Jawaban Soal Nomor 5
Model pada Django disebut sebagai Object-Relational Mapping (ORM) karena adanya kemungkinan bagi pengembang untuk berinteraksi dengan database menggunakan objek pada Python dibandingkan harus menulis query SQL secara langsung. ORM ini menghubungkan tabel-tabel database dengan kelas-kelas Python di mana setiap instance dari kelas mewakili baris dalam tabel tersebut. Dengan ORM, operasi database seperti penyimpanan, pengambilan, dan pembaruan dapat dilakukan dengan metode Python. Selain itu, ORM secara otomatis menangani konversi antara tipe data Python dan tipe data SQL, yang memberikan kemudahan bagi pengembang terhadap pengelolaan data dalam aplikasi.