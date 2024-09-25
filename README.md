- Nama: Nabil Zahid Rahman
- NPM: 2306203324
- Kelas: PBP-A
- Repository: https://github.com/Chromss/e-commerce
- PWS: http://pbp.cs.ui.ac.id/nabil.zahid/homifyinc

# Tugas 4 Checkpoint

### Langkah-langkah dalam mengimplementasikan checklist pada tugas:
1. Membuat sebuah class ProductForm yang terdiri atas 5 atribut, yakni karakter dari setiap objek produk yang akan dibuat (mencakup nama, deskripsi, gambar dari produk, variasi produk, dan harga produk yang menampilkan harga terendah dari variasi yang ada).
2. Mendefinisikan fungsi ```show_xml```, ```show_json```, ```show_xml_by_id```, ```show_json_by_id```, yakni fungsi yang akan memuat informasi dari setiap objek ```Product``` dalam susunan yang lebih easy-access dan versatile.
3. Menambahkan path-path dari fungsi pada nomor (2) untuk dapat diakses dari server yang dijalankan.

### 1. Apa perbedaan antara ```HttpResponseRedirect()``` dan ```redirect()```?  

```HttpResponseRedirect()``` adalah kelas bawaan Django yang digunakan untuk melakukan pengalihan (redirect) pengguna ke URL lain. Saat menggunakan ini, kita harus secara eksplisit menuliskan URL tujuan dalam bentuk string. Di sisi lain, ```redirect()``` adalah shortcut yang lebih fleksibel di Django. Selain menerima string URL, ia juga bisa menerima nama view atau bahkan objek model, dan Django akan secara otomatis mengonversinya menjadi URL yang sesuai.  

### 2. Jelaskan cara kerja penghubungan model ```Product``` dengan ```User```!  

Penghubungan model ```Product``` dengan ```User``` dapat dilakukan dengan menggunakan field ```ForeignKey``` atau ```ManyToManyField```, tergantung kebutuhan. Jika satu pengguna hanya bisa memiliki satu produk atau sekelompok produk tertentu, maka kita menggunakan ```ForeignKey```, yang berarti setiap produk terhubung ke satu pengguna. Namun, jika satu produk bisa dimiliki oleh banyak pengguna dan sebaliknya, maka kita menggunakan ```ManyToManyField```, yang memungkinkan hubungan dua arah antara produk dan pengguna.  

### 3. Apa perbedaan antara authentication dan authorization, dan apa yang terjadi saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

1. **Authentication** adalah proses verifikasi identitas pengguna, yaitu memastikan bahwa mereka adalah orang yang mereka klaim dengan memeriksa kredensial seperti username dan password. Di Django, proses ini dilakukan ketika pengguna mencoba login dengan kredensial yang benar.
   
2. **Authorization** adalah proses pemeriksaan hak akses pengguna terhadap sumber daya atau tindakan tertentu setelah mereka berhasil diotentikasi. Ini menentukan apakah pengguna memiliki izin yang diperlukan untuk mengakses suatu halaman atau fitur.

Saat pengguna login, Django memverifikasi kredensial mereka dengan melakukan otentikasi username dan password. Jika berhasil, Django akan membuat sesi (session) untuk pengguna tersebut, yang menyimpan informasi mereka seperti ID pengguna di database.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

1. Django menggunakan kombinasi sesi (session) dan cookies untuk mengingat pengguna yang sudah login. Setelah pengguna berhasil login, Django membuat session untuk mereka, dan session ID disimpan di dalam cookie pengguna. Pada setiap permintaan berikutnya, session ID ini akan dibawa oleh cookie, sehingga Django dapat mengenali pengguna.

2. Selain untuk mengingat pengguna login, cookies juga digunakan untuk menyimpan preferensi pengguna, melacak aktivitas, atau menyimpan data sesi lainnya yang terkait dengan aplikasi web.

3. Tidak semua cookies aman secara default. Ada beberapa risiko keamanan seperti **session hijacking** (pencurian sesi) atau **cross-site scripting (XSS)**. Namun, Django menyediakan beberapa fitur keamanan untuk cookies, seperti:
   - ```HttpOnly```: Membuat cookie hanya bisa diakses melalui HTTP(S) dan tidak dapat dibaca oleh JavaScript.
   - ```Secure```: Mengharuskan cookie hanya dikirim melalui koneksi HTTPS yang aman.
   - ```SameSite```: Membatasi pengiriman cookie pada permintaan lintas situs (cross-site request), mencegah serangan CSRF.

### Penjelasan Implementasi Kode Pada Tugas 4 ini:

**1. Mengimplementasikan fungsi registrasi, login, dan logout.**
1) Membuat fungsi registrasi
- Aktifkan virtual environment.
- Tambahkan import ```UserCreationForm``` dan ```messages``` pada ```views.py```.
- Tambahkan fungsi ```show_signup``` untuk menghasilkan form registrasi dan membuat akun pengguna setelah submit.
- Buat file HTML baru, ```signup.html```.
- Tambahkan path URL baru untuk fungsi ```show_signup``` di ```urls.py```.

2) Membuat fungsi login
- Tambahkan import ```authenticate```, ```login```, dan ```AuthenticationForm``` ke ```views.py```.
- Buat fungsi ```show_login``` untuk mengautentikasi pengguna.
- Buat file ```login.html``` pada direktori ```templates```.
- Tambahkan path URL untuk fungsi ```show_login``` di ```urls.py```.

3) Membuat fungsi logout
- Tambahkan import ```logout``` di ```views.py```.
- Tambahkan fungsi ```do_logout``` untuk menghapus session pengguna dan cookie ```last_login```.
- Tambahkan path URL untuk fungsi ```do_logout``` di ```urls.py```.

4) Membatasi akses halaman main
- Tambahkan ```@login_required(login_url='/login')``` di atas fungsi ```show_main``` agar hanya pengguna yang login yang bisa mengakses halaman.

**2. Membuat dua akun pengguna dengan masing-masing tiga dummy data.**
- Buat akun pengguna baru dengan username dan password melalui form registrasi di website.
- Tambahkan 3 dummy data produk melalui halaman "Add New Product" dengan memasukkan ```name```, ```section```, ```price```, dan ```description``` untuk setiap produk.

**3. Menghubungkan model ```Product``` dengan ```User```.**
- Pada ```models.py```, impor ```User``` dan tambahkan variabel ```user``` pada class ```Product```.
- Di ```views.py```, ubah fungsi ```show_product``` dengan menambahkan ```commit=False``` pada ```product``` dan hubungkan field ```user``` dengan ```request.user```.
- Ubah context menjadi ```user=request.user``` dan tampilkan ```request.user.username``` di template.
- Simpan perubahan dan jalankan migrasi model.

**4. Menampilkan detail informasi pengguna yang sedang logged in dan menerapkan cookies.**
- Tambahkan ```HttpResponseRedirect```, ```reverse```, dan ```datetime``` pada ```views.py```.
- Di fungsi ```show_login```, tambahkan cookie ```last_login``` untuk menyimpan waktu login terakhir pengguna.
- Tampilkan informasi ```last_login``` pada halaman ```main.html``` melalui context di ```show_main```.
- Ubah fungsi ```do_logout``` untuk menghapus cookie ```last_login``` saat pengguna logout.
- Tambahkan kode HTML di ```main.html``` untuk menampilkan sesi login terakhir.