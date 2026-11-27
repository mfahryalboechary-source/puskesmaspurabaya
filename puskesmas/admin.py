from django.contrib import admin
from .models import InformasiUpdate, JadwalPoli, JadwalPosyanduDesa, SurveiPengaduan


@admin.register(InformasiUpdate)
class InformasiUpdateAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'penulis', 'tanggal_publikasi', 'dipublikasikan')
    list_filter = ('kategori', 'dipublikasikan', 'tanggal_publikasi')
    search_fields = ('judul', 'ringkasan', 'isi_lengkap')
    list_editable = ('dipublikasikan',)


@admin.register(JadwalPoli)
class JadwalPoliAdmin(admin.ModelAdmin):
    list_display = (
        'urutan',
        'nama_poli',
        'klaster',
        'hari_layanan',
        'jam_layanan',
        'nama_dokter',
        'status',
    )
    list_display_links = ('urutan',)
    list_filter = ('klaster', 'status')
    search_fields = ('nama_poli', 'nama_dokter')
    list_editable = ('nama_poli', 'klaster', 'hari_layanan', 'jam_layanan', 'nama_dokter', 'status')


@admin.register(JadwalPosyanduDesa)
class JadwalPosyanduDesaAdmin(admin.ModelAdmin):
    list_display = ('nama_desa', 'nama_posyandu', 'jadwal_minggu', 'jumlah_kader', 'bidan_desa')
    list_display_links = ('nama_desa',)
    list_filter = ('nama_desa',)
    search_fields = ('nama_desa', 'nama_posyandu', 'bidan_desa')
    list_editable = ('nama_posyandu', 'jadwal_minggu', 'jumlah_kader', 'bidan_desa')


@admin.register(SurveiPengaduan)
class SurveiPengaduanAdmin(admin.ModelAdmin):
    list_display = ('nama_warga', 'desa_asal', 'jenis', 'unit_layanan', 'penilaian', 'dibuat_pada')
    list_filter = ('jenis', 'penilaian', 'desa_asal')
    search_fields = ('nama_warga', 'pesan')