- Nama: Nabil Zahid Rahman
- NPM: 2306203324
- Kelas: PBP-A
- Repository: https://github.com/Chromss/e-commerce
- PWS: http://pbp.cs.ui.ac.id/nabil.zahid/homifyinc

# Tugas 5 Checkpoint

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam CSS, jika sebuah elemen memiliki beberapa selector yang diterapkan secara bersamaan, maka urutan prioritas akan mengikuti tingkat spesifisitas masing-masing selector. Urutan tertinggi dimiliki oleh `inline styles`, yaitu gaya yang diterapkan langsung di atribut `style` pada elemen HTML, seperti `<div style="color: red;">`. Setelah itu, prioritas berikutnya adalah `ID selectors` yang ditandai dengan `#` diikuti nama ID, seperti `#navbar`. Selector ini memiliki kekuatan lebih dibandingkan `class selector.`

Selanjutnya, `class selectors, attribute selectors,` dan `pseudo-classes` berada dalam satu tingkatan prioritas, contohnya `.navbar`, `[type="password"]`, atau `:hover`. Urutan terakhir adalah `element selectors` seperti `h1`, serta `pseudo-elements` seperti `::before` dan `::after`. Pada proyek berbasis Django, `inline styles` biasanya tidak digunakan, dan gaya lebih sering diterapkan melalui file CSS terpisah, sehingga `ID selectors, class selectors,` dan `element selectors` lebih umum dijumpai.  

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!  

Responsive design adalah konsep yang penting dalam pengembangan web modern karena memungkinkan tampilan web beradaptasi dengan berbagai perangkat, baik dari segi ukuran layar maupun resolusi. Hal ini menjadi sangat relevan mengingat perangkat yang digunakan pengguna sangat beragam, mulai dari laptop hingga smartphone.

Dengan menggunakan responsive design, web akan tampil lebih rapi dan sesuai dengan desain yang diinginkan di semua perangkat. Sebagai contoh, website seperti Twitter dan Google sudah menerapkan responsive design dengan baik, sehingga tampilannya tetap konsisten di berbagai perangkat. Di sisi lain, beberapa website lama atau web bisnis kecil lokal sering kali tidak memiliki desain yang responsif, sehingga tampilannya tidak optimal saat diakses dari perangkat selain desktop.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

`Margin, border`, dan `padding` merupakan bagian dari `CSS box model` yang digunakan untuk mengatur jarak dan tata letak elemen. `Margin` adalah jarak antara elemen dengan elemen lainnya di luar `border`, misalnya `margin: 16px;` akan menambahkan jarak di semua sisi elemen. `Border` adalah garis yang mengelilingi elemen, misalnya `border: 3px solid black;` akan memberikan garis hitam tebal 3px di sekitar elemen. Sementara itu, `padding` adalah jarak antara konten elemen dengan border elemen tersebut, contohnya `padding: 6px;` akan memberikan jarak 6px di semua sisi konten elemen tersebut. Pengaturan `margin, border`, dan `padding` dapat digunakan bersama-sama untuk menciptakan tata letak yang sesuai dengan kebutuhan tampilan halaman web.

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

`Flexbox` dan `Grid Layout` adalah dua teknik tata letak modern dalam CSS yang sering digunakan untuk membuat desain halaman web yang fleksibel dan responsif. `Flexbox` berfokus pada pengaturan elemen dalam satu baris atau kolom, serta mendistribusikan ruang antar-elemen secara merata menggunakan properti seperti `space-between` dan `space-around`. `Flexbox` sangat cocok untuk menyusun elemen-elemen dalam satu dimensi (horizontal atau vertikal). Di sisi lain, `Grid Layout` memungkinkan pengaturan elemen dalam dua dimensi, yaitu baris dan kolom. Properti seperti `grid-template-columns` dan `grid-template-rows` memungkinkan pengaturan elemen dengan lebih spesifik, sehingga tata letak yang lebih kompleks dapat dibuat dengan mudah.

### Penjelasan Implementasi Kode Pada Tugas 5 ini:

**A. Menambahkan fitur pengubahan dan penghapusan produk**
1. Buat fungsi `edit_product` pada file `views.py` untuk menangani pengeditan data produk. Gunakan `Product.objects.get(pk=id)` untuk mengambil data produk sesuai dengan `id` dari database. Formulir pengeditan kemudian diisi dengan data produk tersebut. Setelah perubahan dilakukan, simpan dengan metode `POST` untuk menyimpan data yang telah diedit.
2. Buat file HTML baru bernama `edit_product.html` yang berisi form untuk mengedit produk. Tambahkan URL yang terhubung dengan halaman ini di `urls.py` dengan mengimpor fungsi edit_product dan menambahkan path `'edit-product/uuid:id'`, misalnya `path('edit-product/uuid:id', edit_product, name='edit_product'),` untuk merujuk ke halaman edit.
3. Buat fungsi `delete_product` pada file `views.py` untuk menghapus data produk. Gunakan `Product.objects.get(pk=id)` untuk mengambil data produk berdasarkan `id` yang dipilih dan gunakan metode `.delete()` untuk menghapusnya dari database.
4. Tambahkan URL untuk memanggil fungsi `delete_product` di `urls.py` dengan path `delete-product/uuid:id'`, seperti `path('delete-product/uuid:id', delete_product, name='delete_product')`. URL ini akan mengarahkan ke fungsi `delete_product` untuk menghapus produk yang dipilih dengan tetap pada `redirect` di `product.html`.

**B. Mengkustomisasi tampilan web dengan Custom CSS styling**
1. Kustomisasi halaman `login.html, signup.html,` dan `add_product.html` dengan menggunakan file CSS yang telah disiapkan pada tag `script`. Hindari penggunaan `form.as_table` pada formulir sehingga setiap elemen form dapat diberikan styling yang unik sesuai pada web HomifyInc.
2. Terapkan styling CSS seperti pengaturan lebar (`width`), tinggi (`height`), dan margin (`margin`) pada form. Bungkus form dalam div terpisah untuk memberikan jarak dan tata letak yang lebih rapi. Sesuaikan bentuk input, button, serta posisi agar form menjadi lebih terstruktur dan menarik.
3. Modifikasi `product.html` untuk menampilkan daftar produk yang responsif. Jika belum ada produk yang tersimpan, tampilkan gambar beserta teks seperti "No Products Available". Gunakan CSS untuk mengatur `size` dan `alignment` gambar agar tampil proporsional.
4. Jika ada produk yang tersimpan, tampilkan setiap produk dalam bentuk card dengan detail informasi produk. Gunakan `div` dengan class khusus untuk membuat desain kartu. Tambahkan dua tombol pada setiap card untuk mengedit dan menghapus produk, yang masing-masing dihubungkan ke URL `edit_product` dan `delete_product` menggunakan `{% url 'main:edit_product' attribute.pk %}` dan `{% url 'main:delete_product' attribute.pk %}`.
5. Kustomisasi elemen navbar pada `main.html` yang berisi navigasi menuju halaman `home, product,` dan `about`. Tambahkan nama user yang sedang login dan tombol logout ketika icon profil ditekan. Gunakan file CSS terpisah untuk memberikan style pada navbar agar tampil menarik dan konsisten.
6. Implementasikan desain responsif khusus pada navbar dan halaman `product.html`. Gunakan `media queries` pada CSS untuk menyesuaikan tampilan navbar pada perangkat yang lebih kecil, seperti mengubah navbar menjadi menu `sidebar`. Sidebar dibuat dengan `div` class dan custom CSS styling. Tambahkan JavaScript untuk memunculkan atau menyembunyikan `sidebar` pada saat tombol menu (hamburger) ditekan.