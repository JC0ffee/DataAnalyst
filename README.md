## Simple Web Scraping

Program ini dibuat untuk melakukan web scraping, yaitu proses otomatis untuk mengambil data dari situs web tertentu. Tujuannya adalah untuk mencari artikel berdasarkan kata kunci yang diberikan oleh pengguna kemudian mengambil informasi seperti judul, isi dan tanggal dari beberapa halaman hasil pencarian di situs tersebut.

**OOP (Object-Oriented Progamming)**

Class Scraper digunakan untuk membuat objek yang bisa melakukan tugas mengambil data dari internet

<p>(__init__) adalah constructor di Python yang dipanggil saat objek baru dibuat dari class Scraper. </p>

<p>self.keywords dan self.pages adalah atribut yang merepresentasikan data yang berkaitan dengan objek tertentu</p>

Sebuah "Scraper" yang di buat berdasarkan kelas ini bisa disebut objek. Objek ini akan memiliki data spesifik seperti kata kunci dan jumlah halaman yang akan diproses.

**Mengambil Data dari Web (fetch)**

Program mengirim permintaan ke internet untuk mengambil data dari halaman web menggunakan _requests_ memasukkan kata kunci pencarian dan nomor halaman yang ingin diambil.

Headers digunakan agar permintaan terlihat seperti berasal dari browser sungguhan, bukan dari robot.

Parameter self.params dikirim sebagai bagian dari permintaan HTTP. Ini adalah cara untuk mengontrol data apa yang ingin kita ambil (misalnya, halaman dan kata kunci pencarian)

(Error Handling) Jika terjadi kesalahan saat mengambil data misalnya koneksi terputus. Dapat ditangani dengan menampilkan pesan tanpa membuat program berhenti

**Mengambil Artikel dari Halaman Web (get_articles)**

(Parsing HTML) Setelah mendapatkan halaman web, harus memecah dan mengurai kode HTML untuk menemukan artikel seperti mencari judul dan isi artikel di dalamnya.

(find_all) Digunakan untuk mencari semua elemen HTML dengan tag tertentu, dalam hal ini _article_. Mencari semua artikel di halaman dan kemudian memprosesnya satu per satu.

(find) Fungsi ini digunakan untuk mencari elemen tertentu di dalam struktur HTML, seperti elemen h3, h2 atau link didalam artikel

(enumerate) Menggunakan loop untuk memproses beberapa halaman sekaligus dan memastikan semua artikel diambil.

**Menampilkan Artikel yang Diambil (show_results)**

Program ini menampilkan hasil scraping kepada pengguna dengan cara yang mudah dibaca. Setiap artikel diberi nomor dan bisa melihat judul serta isinya.

**Menyimpan Artikel ke File (save_file)**

File (Input/Output) adalah cara menyimpan data yang diambil dari internet ke file komputer kita.

Pandas adalah alat yang digunakan untuk memanipulasi data dan mempermudah penyimpanan data ke dalam format tabel.

**Program Utama**

(Procedural Logic) Langkah-langkah program dieksekusi secara linier. OOP dan pemrograman prosedural sering dikombinasikan untuk mendapatkan manfaat dari kedua paradigma.
