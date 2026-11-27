const HEADER_MESSAGES = [
  "Melayani Pasien Dengan Sepenuh Hati ",
  "Integrasi Layanan Primer (ILP) 7 Desa",
  "UGD 24 Jam & Persalinan PONED Siaga",
  "Dinas Kesehatan Kabupaten Sukabumi"
];

const HERO_MESSAGES = [
  "Mewujudkan Masyarakat Kecamatan Purabaya yang Sehat, Mandiri, dan Berkeadilan melalui Pelayanan Kesehatan Primer Bermutu.",
  "Jangkauan Pelayanan Kesehatan Terpadu di 7 Desa dan 48 Posyandu Siklus Hidup Kecamatan Purabaya.",
  "Siaga Kegawatdaruratan Medis 24 Jam (UGD & PONED) serta Rujukan Terintegrasi Kabupaten Sukabumi."
];

function startTypewriter(elementId, messages, speed = 42, pause = 2400) {
  const el = document.getElementById(elementId);
  if (!el) return;
  let msgIndex = 0;
  let charIndex = 0;
  let isDeleting = false;

  function tick() {
    const current = messages[msgIndex];
    if (!isDeleting) {
      el.textContent = current.substring(0, charIndex + 1);
      charIndex++;
      if (charIndex === current.length) {
        isDeleting = true;
        setTimeout(tick, pause);
        return;
      }
    } else {
      el.textContent = current.substring(0, charIndex - 1);
      charIndex--;
      if (charIndex === 0) {
        isDeleting = false;
        msgIndex = (msgIndex + 1) % messages.length;
      }
    }
    setTimeout(tick, isDeleting ? 22 : speed);
  }
  tick();
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function showPage(pageId, subTabId = null) {
  document.querySelectorAll('.page-section').forEach(sec => {
    sec.classList.toggle('active', sec.id === 'page-' + pageId);
  });

  document.querySelectorAll('.nav-link[data-page]').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.page === pageId);
  });

  if (subTabId) {
    switchSubTab(pageId, subTabId);
  }
  window.scrollTo({ top: 0, behavior: 'auto' });
}

function switchSubTab(pageId, subTabId) {
  const container = document.getElementById('page-' + pageId);
  if (!container) return;

  container.querySelectorAll('.subtab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.sub === subTabId);
  });

  container.querySelectorAll('.subtab-panel').forEach(panel => {
    panel.style.display = panel.id === 'sub-' + subTabId ? 'block' : 'none';
  });
}

function renderUpdates(kategoriFilter = 'Semua', keyword = '') {
  const grid = document.getElementById('updatesGrid');
  if (!grid || typeof UPDATES_DATA === 'undefined') return;

  const kw = keyword.toLowerCase().trim();
  const filtered = UPDATES_DATA.filter(item => {
    const matchCat = kategoriFilter === 'Semua' || item.kategori === kategoriFilter;
    const matchKw = !kw || item.judul.toLowerCase().includes(kw) || item.ringkasan.toLowerCase().includes(kw);
    return matchCat && matchKw;
  });

  if (filtered.length === 0) {
    grid.innerHTML = '<div class="card"><p>Belum ada informasi yang sesuai dengan pencarian.</p></div>';
    return;
  }

  grid.innerHTML = filtered.map(item => `
    <article class="card">
      <span class="badge-cat">${item.kategori}</span>
      <div style="font-size:12px;color:#64748b;margin-bottom:6px;">${item.tanggal} • ${item.penulis}</div>
      <h3>${item.judul}</h3>
      <p style="font-size:13px;color:#475569;margin-bottom:14px;">${item.ringkasan}</p>
      <button type="button" class="btn-primary" onclick="bacaDetailUpdate(${item.id})">Baca Selengkapnya</button>
    </article>
  `).join('');
}

function bacaDetailUpdate(id) {
  const item = UPDATES_DATA.find(u => u.id === id);
  if (!item) return;
  document.getElementById('modalJudulUpdate').textContent = item.judul;
  document.getElementById('modalMetaUpdate').textContent = `${item.kategori} • ${item.tanggal} • Oleh ${item.penulis}`;
  document.getElementById('modalIsiUpdate').textContent = item.isi_lengkap;
  document.getElementById('modalDetailUpdate').classList.add('show');
}

function tutupModal(id) {
  document.getElementById(id).classList.remove('show');
}

async function simpanUpdateBaru(e) {
  e.preventDefault();
  const payload = {
    judul: document.getElementById('upJudul').value,
    kategori: document.getElementById('upKategori').value,
    ringkasan: document.getElementById('upRingkasan').value,
    isi_lengkap: document.getElementById('upIsi').value,
    penulis: document.getElementById('upPenulis').value || 'Admin UPTD Puskesmas Purabaya',
  };

  const res = await fetch('/api/update/tambah/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify(payload)
  });
  const data = await res.json();
  if (data.ok) {
    UPDATES_DATA.unshift(data.item);
    renderUpdates('Semua', '');
    document.getElementById('formTambahUpdate').reset();
    tutupModal('modalTambahUpdate');
    alert('Informasi update berhasil dipublikasikan dan tersimpan di database Django!');
  } else {
    alert(data.message || 'Gagal menyimpan informasi.');
  }
}

async function kirimSurveiWarga(e) {
  e.preventDefault();
  const payload = {
    nama_warga: document.getElementById('svNama').value,
    desa_asal: document.getElementById('svDesa').value,
    no_hp: document.getElementById('svHp').value,
    jenis: document.getElementById('svJenis').value,
    unit_layanan: document.getElementById('svUnit').value,
    penilaian: document.getElementById('svPenilaian').value,
    pesan: document.getElementById('svPesan').value,
  };

  const res = await fetch('/api/survei/kirim/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify(payload)
  });
  const data = await res.json();
  if (data.ok) {
    const list = document.getElementById('daftarSurveiTerbaru');
    const cardHtml = `
      <div class="card" style="margin-bottom:10px;padding:14px;">
        <div style="display:flex;justify-content:space-between;font-size:12px;color:#0f766e;font-weight:700;">
          <span>${data.item.nama_warga} (${data.item.desa_asal})</span>
          <span>${data.item.jenis} • ${data.item.penilaian}</span>
        </div>
        <p style="font-size:13px;color:#334155;margin-top:6px;">"${data.item.pesan}"</p>
      </div>
    `;
    list.insertAdjacentHTML('afterbegin', cardHtml);
    document.getElementById('formSurvei').reset();
    alert('Terima kasih! Survei / Pengaduan Anda telah tercatat di database UPTD Puskesmas Purabaya.');
  } else {
    alert(data.message || 'Gagal mengirim survei.');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  // Teks ticker dibuat statis agar tinggi elemen tidak berubah-ubah
  // dan tidak menimbulkan layout shift/gerakan otomatis pada halaman.
  const headerTicker = document.getElementById('headerTicker');
  const heroTicker = document.getElementById('heroTicker');
  if (headerTicker) headerTicker.textContent = HEADER_MESSAGES[0];
  if (heroTicker) heroTicker.textContent = HERO_MESSAGES[0];
  renderUpdates('Semua', '');

  const filterKat = document.getElementById('filterKategoriUpdate');
  const searchInput = document.getElementById('searchUpdateInput');
  if (filterKat) {
    filterKat.addEventListener('change', () => renderUpdates(filterKat.value, searchInput.value));
  }
  if (searchInput) {
    searchInput.addEventListener('input', () => renderUpdates(filterKat.value, searchInput.value));
  }

  const formUp = document.getElementById('formTambahUpdate');
  if (formUp) formUp.addEventListener('submit', simpanUpdateBaru);

  const formSv = document.getElementById('formSurvei');
  if (formSv) formSv.addEventListener('submit', kirimSurveiWarga);
});
