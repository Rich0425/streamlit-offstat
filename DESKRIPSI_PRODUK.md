# 📋 DESKRIPSI PRODUK & PANDUAN PENGGUNAAN DASHBOARD

---

## 🏷️ NAMA DASHBOARD

**"Analisis Kependudukan Jawa Barat 2023–2025: Dasar Perencanaan Fasilitas Kesehatan Berbasis Data"**

---

## 📖 LATAR BELAKANG

Provinsi Jawa Barat adalah provinsi dengan jumlah penduduk terbesar di Indonesia,
mencapai **±50,7 juta jiwa** pada tahun 2025. Dengan pertumbuhan penduduk rata-rata
1,06% per tahun dan distribusi yang tidak merata antara wilayah perkotaan dan pedesaan,
kebutuhan akan fasilitas kesehatan yang memadai semakin mendesak.

Data dari BPS Jawa Barat menunjukkan bahwa terdapat **kesenjangan signifikan**
antara ketersediaan fasilitas kesehatan (RS Umum, Puskesmas, Klinik Pratama, Posyandu)
dengan jumlah penduduk di berbagai kabupaten/kota. Tanpa analisis data yang sistematis,
perencanaan fasilitas kesehatan berisiko tidak tepat sasaran.

Dashboard ini hadir sebagai **alat bantu pengambilan keputusan berbasis data** bagi
pemangku kepentingan: Dinas Kesehatan, Bappeda, DPRD, akademisi, dan masyarakat umum.

---

## 🎯 TUJUAN DASHBOARD

1. **Memvisualisasikan** tren kependudukan dan perkembangan fasilitas kesehatan
   di 27 kabupaten/kota Jawa Barat selama 2023–2025.

2. **Membandingkan** kondisi antar wilayah secara interaktif dan mudah dipahami.

3. **Mengidentifikasi** wilayah yang kekurangan fasilitas kesehatan berdasarkan
   standar Kemenkes RI dan WHO.

4. **Mengelompokkan** wilayah berdasarkan tingkat prioritas kebutuhan fasilitas
   kesehatan menggunakan Machine Learning (K-Means Clustering).

5. **Memberikan rekomendasi** kebijakan yang berbasis data untuk perencanaan
   pembangunan fasilitas kesehatan ke depan.

---

## ✨ KEUNGGULAN DASHBOARD

| Keunggulan | Penjelasan |
|---|---|
| 📊 **5 Tab Analisis Lengkap** | Tren, Perbandingan, Klaster ML, Kecukupan Faskes, Insight & Rekomendasi |
| 🤖 **Machine Learning Terintegrasi** | K-Means Clustering otomatis mengelompokkan 27 wilayah menjadi 3 prioritas |
| 🎛️ **Interaktif & Real-time** | Filter tahun, wilayah, dan variabel — grafik langsung berubah |
| 👶 **Ramah Pengguna Awam** | Setiap grafik dilengkapi penjelasan sederhana; kode warna intuitif |
| 📐 **Berbasis Standar Resmi** | Mengacu standar Kemenkes RI & WHO (1 RS per 240rb penduduk) |
| 🔄 **Data 3 Tahun** | Perbandingan komprehensif 2023–2024–2025 dari sumber resmi BPS |
| 💡 **Insight Otomatis** | Sistem mengidentifikasi temuan kritis secara otomatis dari data |
| 📱 **Responsif** | Tampilan menyesuaikan layar laptop maupun desktop |

---

## 📦 FITUR YANG TERSEDIA

### Tab 1 – 📈 Tren & Pertumbuhan
- Line chart tren penduduk Jawa Barat 2023–2025
- Line chart tren 3 jenis fasilitas kesehatan
- Line chart per wilayah untuk variabel yang dipilih
- Tabel pertumbuhan penduduk dengan kategori (Tinggi/Sedang/Rendah)

### Tab 2 – 📊 Perbandingan Wilayah
- Bar chart horizontal perbandingan variabel terpilih
- Stacked bar chart komposisi faskes per wilayah
- Scatter plot Penduduk vs Total Faskes

### Tab 3 – 🔬 Analisis Klaster (Machine Learning)
- K-Means Clustering otomatis (3 klaster prioritas)
- Scatter plot visualisasi klaster
- Daftar wilayah per kelompok prioritas
- Tabel profil rata-rata per klaster

### Tab 4 – 🩺 Kecukupan Fasilitas Kesehatan
- Indikator jumlah wilayah kekurangan RS & Puskesmas
- Bar chart rasio RS Umum vs standar minimum
- Tabel lengkap status kecukupan per wilayah
- Scatter plot kepadatan vs total faskes

### Tab 5 – 💡 Insight & Rekomendasi
- 6 temuan utama otomatis dari data
- 4 rekomendasi kebijakan terstruktur
- Sumber data dan metodologi

---

## 🗂️ SUMBER DATA

| File | Deskripsi |
|---|---|
| `Jumlah_RS_..._2023.csv` | Data fasilitas kesehatan Jawa Barat 2023 (BPS) |
| `Jumlah_RS_..._2024.csv` | Data fasilitas kesehatan Jawa Barat 2024 (BPS) |
| `Jumlah_RS_..._2025.csv` | Data fasilitas kesehatan Jawa Barat 2025 (BPS) |
| `Penduduk_..._2023.csv`  | Data kependudukan Jawa Barat 2023 (BPS) |
| `Penduduk_..._2024.csv`  | Data kependudukan Jawa Barat 2024 (BPS) |
| `Penduduk_..._2025.csv`  | Data kependudukan Jawa Barat 2025 (BPS) |

**Sumber:** Badan Pusat Statistik (BPS) Provinsi Jawa Barat

---

## 🚀 PANDUAN INSTALASI & MENJALANKAN

### Langkah 1 – Pastikan Python sudah terpasang
```
python --version
# Harus Python 3.8 atau lebih baru
```

### Langkah 2 – Install semua library yang dibutuhkan
```bash
pip install streamlit pandas numpy plotly scikit-learn
```

### Langkah 3 – Jalankan dashboard
```bash
streamlit run app.py
```

### Langkah 4 – Buka di browser
Browser akan terbuka otomatis di:
```
http://localhost:8501
```
Jika tidak terbuka otomatis, salin alamat tersebut ke browser Anda.

---

## 🎮 CARA MENGGUNAKAN DASHBOARD

### Sidebar (Panel Kiri)
| Kontrol | Fungsi |
|---|---|
| 🗓️ **Filter Tahun** | Pilih satu atau beberapa tahun (2023/2024/2025) |
| 🗺️ **Filter Wilayah** | Pilih Semua / Kabupaten saja / Kota saja |
| 📋 **Pilih Wilayah** | Centang spesifik kabupaten/kota yang ingin dilihat |
| 📊 **Dropdown Variabel** | Pilih variabel yang ingin divisualisasikan |

### Navigasi Tab
Klik tab di bagian atas untuk berpindah antar analisis.

### Membaca Kode Warna
- 🔴 **Merah** = Kondisi kritis, butuh perhatian segera
- 🟡 **Kuning** = Perlu dimonitor dan diperbaiki
- 🟢 **Hijau** = Kondisi baik dan memenuhi standar

---

## 🧠 METODOLOGI ANALISIS

### 1. Klasterisasi K-Means
- **Algoritma:** K-Means Clustering (scikit-learn)
- **Fitur input:** Jumlah penduduk, kepadatan, RSU, Puskesmas, Klinik, Rasio RSU/100rb, Rasio PKM/100rb
- **Jumlah klaster:** 3 (Prioritas Tinggi, Sedang, Rendah)
- **Normalisasi:** StandardScaler untuk menyeimbangkan skala antar variabel

### 2. Standar Kecukupan Faskes
- **RS Umum:** ≥ 0,42 per 100.000 penduduk (Permenkes No. 3 Tahun 2020)
- **Puskesmas:** ≥ 3,33 per 100.000 penduduk (1 per 30.000 penduduk)

### 3. Indikator Kunci
- Rasio RSU per 100.000 penduduk
- Rasio Puskesmas per 100.000 penduduk
- Laju pertumbuhan penduduk tahunan
- Kepadatan penduduk per km²

---

## 🛠️ TEKNOLOGI YANG DIGUNAKAN

| Library | Versi | Fungsi |
|---|---|---|
| `streamlit` | ≥ 1.28 | Framework dashboard web |
| `pandas` | ≥ 1.5 | Pengolahan data tabular |
| `numpy` | ≥ 1.23 | Komputasi numerik |
| `plotly` | ≥ 5.14 | Visualisasi interaktif |
| `scikit-learn` | ≥ 1.2 | Machine Learning (K-Means) |

---

## 👥 TARGET PENGGUNA

- **Dinas Kesehatan Jawa Barat** — perencanaan dan evaluasi program
- **Bappeda Jawa Barat** — dasar penyusunan RPJMD bidang kesehatan
- **DPRD / Legislatif** — pengawasan anggaran kesehatan daerah
- **Akademisi & Peneliti** — studi kesehatan masyarakat
- **Mahasiswa** — pembelajaran analisis data kesehatan
- **Masyarakat Umum** — mengetahui kondisi faskes di daerahnya

---

*Dashboard ini bersifat open-source dan dapat dikembangkan lebih lanjut.*
*Selalu perbarui data secara berkala dengan publikasi BPS terbaru.*
