import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import InformasiUpdate, JadwalPoli, JadwalPosyanduDesa, SurveiPengaduan


def seed_initial_data():
    if not InformasiUpdate.objects.exists():
        InformasiUpdate.objects.bulk_create([
            InformasiUpdate(
                judul='Jadwal Pekan Imunisasi & Posyandu Terintegrasi 7 Desa Kecamatan Purabaya',
                kategori='Pengumuman',
                ringkasan='Pelaksanaan pelayanan Posyandu siklus hidup (bayi, balita, ibu hamil, remaja, dan lansia) serentak di 45 Posyandu.',
                isi_lengkap='UPTD Puskesmas Purabaya menginformasikan kepada seluruh masyarakat di 7 desa wilayah kerja (Purabaya, Neglasari, Pagelaran, Citamiang, Cicukang, Cimerang, dan Margaluyu) bahwa kegiatan Posyandu Integrasi Layanan Primer (ILP) dilaksanakan sesuai jadwal masing-masing RW. Harap membawa buku KIA dan KTP/KK.',
                penulis='Koordinator UKM & Promkes'
            ),
            InformasiUpdate(
                judul='Layanan UGD 24 Jam dan Persalinan PONED Siaga Penuh',
                kategori='Berita Kegiatan',
                ringkasan='Unit Gawat Darurat (UGD) dan Ruang Bersalin PONED UPTD Puskesmas Purabaya siap melayani kegawatdaruratan medis 24 jam nonstop.',
                isi_lengkap='Untuk meningkatkan keselamatan ibu dan bayi serta penanganan kegawatdaruratan masyarakat Kecamatan Purabaya, tim medis jaga UGD 24 Jam beserta layanan ambulans rujukan siaga penuh setiap hari termasuk hari libur nasional. Hubungi Call Center UGD: (0266) 341-119.',
                penulis='Penanggung Jawab Klaster Pelayanan'
            ),
            InformasiUpdate(
                judul='Edukasi Pencegahan DBD (3M Plus) dan Skrining Hipertensi Usia Produktif',
                kategori='Edukasi Kesehatan',
                ringkasan='Waspada perubahan cuaca dengan gerakan Pemberantasan Sarang Nyamuk (PSN) serta cek tekanan darah rutin gratis.',
                isi_lengkap='Masyarakat diimbau rutin menguras tempat penampungan air, menutup rapat wadah air, dan mendaur ulang barang bekas (3M Plus). Selain itu, warga usia 15 tahun ke atas dapat melakukan skrining PTM (tekanan darah dan gula darah) secara gratis di Klaster 3 UPTD Puskesmas Purabaya.',
                penulis='Tim Surveilans & P2P'
            ),
        ])

    if not JadwalPoli.objects.exists():
        JadwalPoli.objects.bulk_create([
            JadwalPoli(urutan=1, nama_poli='Klaster 2 - Poli Kesehatan Ibu, Anak & Remaja', klaster='Klaster 2', hari_layanan='Senin - Sabtu', jam_layanan='08.00 - 13.30 WIB', nama_dokter='dr. Rina Marlina & Bidan Koordinator', status='Buka'),
            JadwalPoli(urutan=2, nama_poli='Klaster 3 - Poli Umum Dewasa & Lansia', klaster='Klaster 3', hari_layanan='Senin - Sabtu', jam_layanan='08.00 - 14.00 WIB', nama_dokter='dr. Hendra Gunawan', status='Buka'),
            JadwalPoli(urutan=3, nama_poli='Poli Kesehatan Gigi & Mulut', klaster='Klaster 2 & 3', hari_layanan='Senin - Kamis', jam_layanan='08.00 - 13.00 WIB', nama_dokter='drg. Siti Nurhaliza', status='Buka'),
            JadwalPoli(urutan=4, nama_poli='Klaster 4 - Poli TB, DOTS & Penyakit Menular', klaster='Klaster 4', hari_layanan='Selasa & Jumat', jam_layanan='08.00 - 13.00 WIB', nama_dokter='dr. Ahmad Fauzi', status='Buka'),
            JadwalPoli(urutan=5, nama_poli='Laboratorium, Gizi & Konseling Sanitasi', klaster='Lintas Klaster', hari_layanan='Senin - Sabtu', jam_layanan='08.00 - 14.00 WIB', nama_dokter='Tim Analis & Nutrisionis', status='Buka'),
            JadwalPoli(urutan=6, nama_poli='UGD 24 Jam & Persalinan PONED', klaster='Lintas Klaster', hari_layanan='Setiap Hari (24 Jam)', jam_layanan='00.00 - 24.00 WIB', nama_dokter='Dokter & Bidan Jaga UGD', status='Siaga 24 Jam'),
        ])

    if not JadwalPosyanduDesa.objects.exists():
        JadwalPosyanduDesa.objects.bulk_create([
            JadwalPosyanduDesa(nama_desa='Desa Purabaya', nama_posyandu='Posyandu Melati 1 - 8', jadwal_minggu='Minggu ke-1 Setiap Bulan', jumlah_kader=40, bidan_desa='Bd. Nining Suryani, A.Md.Keb'),
            JadwalPosyanduDesa(nama_desa='Desa Neglasari', nama_posyandu='Posyandu Mawar 1 - 7', jadwal_minggu='Minggu ke-1 Setiap Bulan', jumlah_kader=35, bidan_desa='Bd. Ai Ratnasari, A.Md.Keb'),
            JadwalPosyanduDesa(nama_desa='Desa Pagelaran', nama_posyandu='Posyandu Kenanga 1 - 6', jadwal_minggu='Minggu ke-2 Setiap Bulan', jumlah_kader=30, bidan_desa='Bd. Lilis Karlina, A.Md.Keb'),
            JadwalPosyanduDesa(nama_desa='Desa Citamiang', nama_posyandu='Posyandu Anggrek 1 - 6', jadwal_minggu='Minggu ke-2 Setiap Bulan', jumlah_kader=30, bidan_desa='Bd. Dewi Sartika, A.Md.Keb'),
            JadwalPosyanduDesa(nama_desa='Desa Cicukang', nama_posyandu='Posyandu Dahlia 1 - 6', jadwal_minggu='Minggu ke-3 Setiap Bulan', jumlah_kader=30, bidan_desa='Bd. Rini Anggraeni, A.Md.Keb'),
            JadwalPosyanduDesa(nama_desa='Desa Cimerang', nama_posyandu='Posyandu Teratai 1 - 6', jadwal_minggu='Minggu ke-3 Setiap Bulan', jumlah_kader=30, bidan_desa='Bd. Yanti Susanti, A.Md.Keb'),
            JadwalPosyanduDesa(nama_desa='Desa Margaluyu', nama_posyandu='Posyandu Flamboyan 1 - 6', jadwal_minggu='Minggu ke-4 Setiap Bulan', jumlah_kader=30, bidan_desa='Bd. Fitriani, A.Md.Keb'),
        ])


def beranda(request):
    seed_initial_data()
    updates = InformasiUpdate.objects.filter(dipublikasikan=True)
    jadwal_poli = JadwalPoli.objects.all()
    posyandu_list = JadwalPosyanduDesa.objects.all()
    survei_terbaru = SurveiPengaduan.objects.all()[:6]

    updates_json = json.dumps([
        {
            'id': u.id,
            'judul': u.judul,
            'kategori': u.kategori,
            'ringkasan': u.ringkasan,
            'isi_lengkap': u.isi_lengkap,
            'penulis': u.penulis,
            'tanggal': u.tanggal_publikasi.strftime('%d %b %Y'),
        }
        for u in updates
    ])

    context = {
        'updates': updates,
        'updates_json': updates_json,
        'jadwal_poli': jadwal_poli,
        'posyandu_list': posyandu_list,
        'survei_terbaru': survei_terbaru,
        'total_responden': 248 + SurveiPengaduan.objects.count(),
    }
    return render(request, 'puskesmas/index.html', context)


@require_POST
def api_tambah_update(request):
    try:
        data = json.loads(request.body)
        judul = data.get('judul', '').strip()
        kategori = data.get('kategori', 'Pengumuman').strip()
        ringkasan = data.get('ringkasan', '').strip()
        isi_lengkap = data.get('isi_lengkap', '').strip() or ringkasan
        penulis = data.get('penulis', 'Admin UPTD Puskesmas Purabaya').strip()

        if not judul or not ringkasan:
            return JsonResponse({'ok': False, 'message': 'Judul dan ringkasan wajib diisi.'}, status=400)

        item = InformasiUpdate.objects.create(
            judul=judul,
            kategori=kategori,
            ringkasan=ringkasan,
            isi_lengkap=isi_lengkap,
            penulis=penulis,
        )
        return JsonResponse({
            'ok': True,
            'item': {
                'id': item.id,
                'judul': item.judul,
                'kategori': item.kategori,
                'ringkasan': item.ringkasan,
                'isi_lengkap': item.isi_lengkap,
                'penulis': item.penulis,
                'tanggal': item.tanggal_publikasi.strftime('%d %b %Y'),
            }
        })
    except Exception as e:
        return JsonResponse({'ok': False, 'message': str(e)}, status=400)


@require_POST
def api_kirim_survei(request):
    try:
        data = json.loads(request.body)
        nama_warga = data.get('nama_warga', '').strip()
        desa_asal = data.get('desa_asal', 'Purabaya').strip()
        no_hp = data.get('no_hp', '').strip()
        jenis = data.get('jenis', 'Survei IKM').strip()
        unit_layanan = data.get('unit_layanan', 'Pelayanan Umum').strip()
        penilaian = data.get('penilaian', 'Sangat Puas').strip()
        pesan = data.get('pesan', '').strip()

        if not nama_warga or not pesan:
            return JsonResponse({'ok': False, 'message': 'Nama warga dan pesan wajib diisi.'}, status=400)

        obj = SurveiPengaduan.objects.create(
            nama_warga=nama_warga,
            desa_asal=desa_asal,
            no_hp=no_hp,
            jenis=jenis,
            unit_layanan=unit_layanan,
            penilaian=penilaian,
            pesan=pesan,
        )
        return JsonResponse({
            'ok': True,
            'item': {
                'nama_warga': obj.nama_warga,
                'desa_asal': obj.desa_asal,
                'jenis': obj.jenis,
                'unit_layanan': obj.unit_layanan,
                'penilaian': obj.penilaian,
                'pesan': obj.pesan,
                'tanggal': obj.dibuat_pada.strftime('%d %b %Y'),
            }
        })
    except Exception as e:
        return JsonResponse({'ok': False, 'message': str(e)}, status=400)
