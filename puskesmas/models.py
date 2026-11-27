from django.db import models


class InformasiUpdate(models.Model):
    KATEGORI_CHOICES = [
        ('Pengumuman', 'Pengumuman'),
        ('Berita Kegiatan', 'Berita Kegiatan'),
        ('Edukasi Kesehatan', 'Edukasi Kesehatan'),
    ]

    judul = models.CharField(max_length=200)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES, default='Pengumuman')
    ringkasan = models.TextField()
    isi_lengkap = models.TextField()
    penulis = models.CharField(max_length=100, default='Tim Promkes UPTD Puskesmas Purabaya')
    tanggal_publikasi = models.DateField(auto_now_add=True)
    dipublikasikan = models.BooleanField(default=True)

    class Meta:
        ordering = ['-tanggal_publikasi', '-id']
        verbose_name = 'Informasi Update'
        verbose_name_plural = 'Informasi Update'

    def __str__(self):
        return f"[{self.kategori}] {self.judul}"


class JadwalPoli(models.Model):
    KLASTER_CHOICES = [
        ('Klaster 1', 'Klaster 1'),
        ('Klaster 2', 'Klaster 2'),
        ('Klaster 3', 'Klaster 3'),
    ]

    nama_poli = models.CharField(max_length=120)
    klaster = models.CharField(max_length=30, choices=KLASTER_CHOICES, default='Klaster 2')
    hari_layanan = models.CharField(max_length=100, default='Senin - Sabtu')
    jam_layanan = models.CharField(max_length=100, default='08.00 - 14.00 WIB')
    nama_dokter = models.CharField(max_length=150)
    status = models.CharField(max_length=50, default='Buka')
    urutan = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['urutan', 'id']
        verbose_name = 'Jadwal Poli & Dokter'
        verbose_name_plural = 'Jadwal Poli & Dokter'

    def __str__(self):
        return f"{self.nama_poli} ({self.klaster}) - {self.nama_dokter}"


class JadwalPosyanduDesa(models.Model):
    nama_desa = models.CharField(max_length=100)
    nama_posyandu = models.CharField(max_length=120)
    jadwal_minggu = models.CharField(max_length=100, default='Minggu ke-1 Setiap Bulan')
    jumlah_kader = models.PositiveIntegerField(default=5)
    bidan_desa = models.CharField(max_length=120)
    fokus_layanan = models.CharField(max_length=200, default='Balita, Ibu Hamil, Remaja & Lansia (ILP)')

    class Meta:
        ordering = ['nama_desa', 'nama_posyandu']
        verbose_name = 'Posyandu Desa'
        verbose_name_plural = 'Data Posyandu 7 Desa'

    def __str__(self):
        return f"{self.nama_posyandu} ({self.nama_desa})"


class SurveiPengaduan(models.Model):
    JENIS_CHOICES = [
        ('Survei IKM', 'Survei Kepuasan Masyarakat (IKM)'),
        ('Pengaduan', 'Pengaduan Layanan'),
        ('Saran', 'Saran & Apresiasi'),
    ]

    PENILAIAN_CHOICES = [
        ('Sangat Puas', 'Sangat Puas (4)'),
        ('Puas', 'Puas (3)'),
        ('Cukup Puas', 'Cukup Puas (2)'),
        ('Tidak Puas', 'Tidak Puas (1)'),
    ]

    nama_warga = models.CharField(max_length=120)
    desa_asal = models.CharField(max_length=100, blank=True, default='Purabaya')
    no_hp = models.CharField(max_length=25, blank=True, default='')
    jenis = models.CharField(max_length=30, choices=JENIS_CHOICES, default='Survei IKM')
    unit_layanan = models.CharField(max_length=100, default='Pelayanan Umum')
    penilaian = models.CharField(max_length=30, choices=PENILAIAN_CHOICES, default='Sangat Puas')
    pesan = models.TextField()
    tanggapan_admin = models.TextField(blank=True, default='')
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-dibuat_pada']
        verbose_name = 'Survei IKM & Pengaduan'
        verbose_name_plural = 'Hasil Survei IKM & Pengaduan'

    def __str__(self):
        return f"{self.nama_warga} - {self.jenis} ({self.penilaian})"