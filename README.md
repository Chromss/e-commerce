- Nama: Nabil Zahid Rahman
- NPM: 2306203324
- Kelas: PBP-A
- Repository: https://github.com/Chromss/e-commerce
- PWS: http://pbp.cs.ui.ac.id/nabil.zahid/homifyinc

## Tugas 6 Checkpoint

### 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

JavaScript memiliki peran penting dalam pengembangan aplikasi web modern karena kemampuannya untuk meningkatkan interaktivitas dan pengalaman pengguna pada halaman web. Dengan JavaScript, kita dapat menciptakan elemen dinamis, seperti memuat data secara asinkron tanpa harus me-refresh halaman, memvalidasi input pengguna secara real-time, dan menambahkan animasi yang menarik. Hal ini menjadikan website lebih responsif dan interaktif sehingga pengguna dapat berinteraksi dengan konten secara lebih intuitif dan efisien.

### 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await?`  

Statement `await` digunakan untuk menunggu hasil dari sebuah proses asinkron sebelum melanjutkan ke baris kode berikutnya. Dalam konteks `fetch()`, `await` memastikan bahwa kita menunggu hingga respons dari server diterima sebelum melanjutkan untuk memproses data tersebut. Jika `await` tidak digunakan, kode akan berjalan secara sinkron tanpa menunggu hasil dari `fetch()` yang berpotensi menyebabkan error atau hasil yang tidak diharapkan disebabkan proses data mungkin terjadi sebelum respons sepenuhnya diterima.

### 3. Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?

Decorator `@csrf_exempt` digunakan untuk menonaktifkan pengecekan token CSRF (Cross-Site Request Forgery) pada view yang akan menerima request AJAX `POST`. Hal ini bermanfaat jika kita mengirimkan request AJAX dari sumber yang tidak terintegrasi dengan mekanisme CSRF token, seperti aplikasi klien pihak ketiga atau request eksternal lainnya. Namun, penggunaannya perlu dibatasi pada view-view tertentu saja untuk menghindari celah keamanan yang bisa dimanfaatkan oleh penyerang. Secara umum, disarankan untuk tetap menggunakan proteksi CSRF di kebanyakan view.

### 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Meskipun validasi input di frontend dapat memberikan respons cepat dan pengalaman pengguna yang lebih baik, proses validasi dan pembersihan data harus tetap dilakukan di backend. Hal ini dikarenakan data yang dikirimkan dari frontend bisa dimanipulasi atau diubah oleh pengguna atau pihak ketiga sebelum mencapai server. Jika hanya mengandalkan validasi di frontend, aplikasi akan rentan terhadap serangan seperti injection atau manipulasi data lainnya. Oleh karena itu, backend berperan penting dalam menjaga integritas data dan keamanan aplikasi dengan melakukan validasi dan pembersihan sebagai lapisan perlindungan tambahan.

### Penjelasan Implementasi Kode Pada Tugas 6 ini:

**A. AJAX `GET`**
1. Sesuaikan kode HTML yang menampilkan daftar produk agar dapat bekerja dengan request AJAX `GET`. Pastikan semua elemen yang merepresentasikan kartu produk sudah memiliki ID atau kelas yang dapat diakses melalui JavaScript.
2. Buat fungsi `getProducts()` pada bagian bawah file HTML. Fungsi ini akan dipanggil untuk mengambil data produk dari backend menggunakan AJAX `GET`.
3. Gunakan `fetch()` dengan metode `GET` untuk mengambil data produk dari endpoint `show_json`. Setelah respons diterima, tampilkan data yang diterima ke dalam elemen HTML menggunakan innerHTML untuk memperbarui tampilan produk secara dinamis.
4. Pastikan data yang diambil oleh `getProducts()` hanya mencakup produk milik pengguna yang sedang login. Ini bisa diatur dengan menyesuaikan filter data di view `show_json` di Django backend, yakni `data = Attribute.objects.filter(user=request.user)`.
5. Buat view baru di `views.py` bernama show_json. View ini akan menampilkan data produk dalam format JSON dan hanya menampilkan produk milik pengguna yang sedang login.

**B. AJAX `POST`**
1. Tambahkan sebuah tombol pada template HTML yang akan memunculkan modal berisi form input untuk menambahkan produk baru. Ketika tombol ini diklik, modal akan ditampilkan agar pengguna dapat memasukkan detail produk.
2. Tambahkan fungsi view di views.py yang menangani permintaan `POST` untuk menambahkan produk baru ke dalam database. View ini akan menerima data form dari frontend dan menyimpannya ke dalam database.
3. Di `urls.py`, buat path baru `add-inventory-direct` yang akan mengarah ke fungsi view yang menangani penambahan produk baru. Pastikan path ini terhubung dengan view yang baru saja dibuat.
4. Di dalam modal form HTML, tambahkan AJAX `POST` yang akan mengirimkan data form ke path `add-inventory-direct` tanpa me-reload halaman. Ketika form dikirimkan, AJAX akan memastikan data diteruskan ke backend untuk disimpan.
5. Setelah produk baru berhasil ditambahkan, buat fungsi `refreshProducts()` untuk memperbarui daftar produk di halaman tanpa me-reload seluruh halaman. Fungsi ini dapat mengirim request `GET` via AJAX untuk mengambil daftar produk terbaru, kemudian memperbarui tampilan produk di halaman.