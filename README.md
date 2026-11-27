# Website Resmi UPTD Puskesmas Purabaya (Django - v3)

Project full-stack **Django** siap pakai untuk dibuka di **VS Code**, dengan pembaruan tata letak header sehingga:
1. Identitas **UPTD Puskesmas Purabaya**, **Dinas Kesehatan Kabupaten Sukabumi**, serta kotak teks bergerak di bawahnya tampil utuh tanpa terpotong (`flex-shrink: 0` dan `white-space: nowrap`).
2. Seluruh deretan menu (**Beranda** hingga **Survei IKM & Pengaduan**) bergeser rapat ke kanan (`margin-left: auto`).
3. Bagian tabel Jadwal Pelayanan & Dokter dihapus dari halaman Beranda dan dipusatkan di menu **Layanan Kesehatan > Jadwal Poli & Dokter**.

## Cara Menjalankan di VS Code
1. Ekstrak `web_puskesmas_purabaya_django_v3.zip` lalu buka folder `web_puskesmas_purabaya` di **VS Code** (`File > Open Folder`).
2. Buka Terminal di VS Code (`Ctrl + ~`), buat dan aktifkan virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install Django:
   ```bash
   pip install -r requirements.txt
   ```
4. Buat database SQLite dan akun admin petugas puskesmas:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Jalankan server:
   ```bash
   python manage.py runserver
   ```
6. Buka di browser:
   - **Halaman Website Puskesmas:** `http://127.0.0.1:8000/`
   - **Dashboard Admin Puskesmas:** `http://127.0.0.1:8000/admin/`
