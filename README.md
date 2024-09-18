- Nama: Nabil Zahid Rahman
- NPM: 2306203324
- Kelas: PBP-A

# Tugas 3 Checkpoint

### Langkah-langkah dalam mengimplementasikan checklist pada tugas:
1. Membuat sebuah class ProductForm yang terdiri atas 5 atribut, yakni karakter dari setiap objek produk yang akan dibuat (mencakup nama, deskripsi, gambar dari produk, variasi produk, dan harga produk yang menampilkan harga terendah dari variasi yang ada).
2. Mendefinisikan fungsi ```show_xml```, ```show_json```, ```show_xml_by_id```, ```show_json_by_id```, yakni fungsi yang akan memuat informasi dari setiap objek ```Product``` dalam susunan yang lebih easy-access dan versatile.
3. Menambahkan path-path dari fungsi pada nomor (2) untuk dapat diakses dari server yang dijalankan.

### 1. Mengapa kita memerlukan data delivery dalam sebuah platform?
Dalam pengembangan platform, kita perlu mengirim data (seperti HTML, XML, atau JSON) antara berbagai bagian sistem agar platform tersebut menjadi responsif dan dapat menyesuaikan interaksi pengguna. Hal Ini penting untuk memisahkan logika bisnis (seperti yang ada di views.py) dari tampilan yang biasanya berada pada direktori templates. Dengan dilakukannya pengiriman data, halaman web dapat diperbarui secara otomatis sesuai perubahan data tanpa perlu mengubah struktur HTML secara manual. Oleh karena itu, data delivery menjadi penting agar front-end dan back-end dapat terintegrasi dengan baik.

### 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dari XML?
JSON lebih disukai karena lebih efisien dan mudah dibaca dengan formatnya yang sederhana, menggunakan pasangan "key":"value". JSON juga mendukung struktur data yang kompleks seperti objek, array, dan nilai primitif, sedangkan XML cenderung kurang fleksibel dalam menangani data kompleks. Selain itu, banyak bahasa pemrograman yang mendukung parsing JSON dengan mudah, seperti JavaScript yang memiliki fungsi JSON.parse() dan JSON.stringify() untuk menangani data JSON.

### 3. Apa fungsi dari method is_valid() pada form Django dan mengapa dibutuhkan?
Method is_valid() pada form Django digunakan untuk memvalidasi data yang diisi oleh pengguna. Fungsinya adalah memastikan bahwa data yang dikirimkan sesuai dengan aturan dan tipe data yang telah ditetapkan pada form. Contohnya, jika suatu field harus berisi angka (IntegerField), method ini akan memeriksa apakah input tersebut memang bertipe integer. Jika semua data sesuai, method ini akan mengembalikan nilai True, sebaliknya jika ada kesalahan, nilai yang dikembalikan adalah False. Fungsi ini penting untuk menjaga agar hanya data valid yang disimpan ke database serta mencegah serangan seperti SQL Injection atau XSS.

### 4. Mengapa kita membutuhkan csrf_token pada form di Django dan apa risikonya jika tidak digunakan?
csrf_token adalah mekanisme keamanan yang melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Ini penting saat pengguna mengirimkan form yang memerlukan autentikasi, seperti form login atau form yang memodifikasi data di database. Django menggunakan token unik untuk setiap sesi, dan token ini diverifikasi di server setiap kali form dikirim. Jika token yang diterima tidak sesuai dengan yang disimpan di server, permintaan akan ditolak. Jika kita tidak menambahkan csrf_token, aplikasi akan menjadi rentan terhadap serangan CSRF, di mana penyerang bisa mengirim permintaan palsu atas nama pengguna tanpa sepengetahuan mereka. Ini bisa disalahgunakan oleh penyerang untuk melakukan tindakan yang merugikan pengguna, seperti mengubah data penting atau melakukan transaksi tidak sah.

### 5. Dokumentasi
![xml](media/xmlview.png)
![xml](media/xmlbyid_view.png)
![xml](media/jsonview.png)
![xml](media/jsonbyid_view.png)