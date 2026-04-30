# 📄 PROPOSAL — AI Impact Challenge Datathon

> **Copy isi ini ke Google Docs template yang udah di-copy dari link kompetisi.**
> **Ganti bagian `[NAMA]`, `[EMAIL]`, dan `[LINK]` sesuai data lo.**

---

## Informasi Peserta

| No | Nama | Email Dicoding |
|----|------|----------------|
| 1  | [NAMA 1] | [EMAIL DICODING 1] |
| 2  | [NAMA 2 - jika tim] | [EMAIL 2] |
| 3  | [NAMA 3 - jika tim] | [EMAIL 3] |

**Topik: Urban Resilience & Smart City**

---

## Ringkasan Eksekutif
*(maks. 2000 karakter)*

**Problem Statement:**
Gedung kantor pemerintah di Indonesia mengonsumsi 4.995,12 GWh listrik per tahun, dimana DKI Jakarta sendiri menyerap 1.396,61 GWh — setara 28% konsumsi gedung pemerintah nasional (Statistik PLN 2022, Tabel 6). Angka ini menjadikan Jakarta sebagai episentrum konsumsi energi gedung publik di Indonesia. Kementerian ESDM mengidentifikasi potensi penghematan energi pada bangunan gedung sebesar 10–30%, yang berarti DKI Jakarta berpotensi menghemat 139–419 GWh per tahun atau setara Rp195–587 miliar (asumsi tarif P Rp1.400/kWh). Namun mayoritas gedung pemerintah belum memiliki sistem monitoring energi berbasis data dan belum menerapkan audit energi secara konsisten (PP No. 33 Tahun 2023 tentang Konservasi Energi).

**Research Questions:**
1. Bagaimana pola konsumsi energi gedung non-residensial dipengaruhi oleh tipe bangunan, cuaca, dan karakteristik fisik bangunan?
2. Bagaimana model prediktif berbasis Machine Learning dapat mengidentifikasi inefisiensi dan mendeteksi anomali konsumsi energi pada gedung publik di kawasan perkotaan tropis seperti Jakarta?
3. Seberapa besar potensi penghematan energi yang terukur jika rekomendasi AI diterapkan pada gedung pemerintah DKI Jakarta?

**Latar Belakang:**
Indonesia berkomitmen mencapai Net Zero Emission 2060 dengan target pengurangan 25% konsumsi energi bangunan pada 2030 (GlobalABC Roadmap Indonesia). Efisiensi energi berkontribusi ~37% reduksi emisi sektor energi (NDC Indonesia). Untuk mendukung target ini, dibutuhkan sistem cerdas berbasis AI yang mampu menganalisis pola konsumsi, mendeteksi pemborosan, dan memberikan rekomendasi penghematan secara otomatis. Proyek ini memanfaatkan dataset BDG2 (Building Data Genome Project 2) dari Nature Scientific Data — 3.053 meter energi dari 1.636 gedung — untuk membangun model AI yang dikontekstualisasi ke gedung pemerintah Jakarta menggunakan data cuaca lokal dan standar IKE Indonesia.

---

## Deskripsi Project

**Nama Produk:** APBN_ai — *AI-Powered Building Energy Anomaly Detection & Optimization for Urban Resilience*

**Fungsi:** Platform berbasis web yang mengintegrasikan Artificial Intelligence untuk melakukan prediksi konsumsi energi, deteksi anomali, dan memberikan rekomendasi penghematan energi pada gedung-gedung publik/pemerintah di kawasan perkotaan Jakarta.

**Cara Menyelesaikan Masalah:**

APBN_ai menyelesaikan masalah inefisiensi energi gedung pemerintah melalui pendekatan 3 tahap:

1. **Analisis Pola (Descriptive):** Menggunakan dataset BDG2 (53,6 juta data hourly dari 1.636 gedung non-residensial) untuk memahami pola universal konsumsi energi berdasarkan tipe gedung, cuaca, dan karakteristik fisik bangunan. Data diproses melalui Exploratory Data Analysis mendalam dengan feature engineering berbasis domain knowledge ketenagalistrikan — termasuk log-transformasi luas bangunan, usia gedung, rata-rata luas per lantai, interaksi tipe × luas, integrasi data cuaca (suhu rata-rata & deviasi), dan building clustering menggunakan K-Means.

2. **Prediksi & Deteksi Anomali (Predictive):** Melatih model Machine Learning menggunakan pendekatan ensemble gradient boosting (GradientBoostingRegressor dengan hyperparameter tuning via RandomizedSearchCV) untuk forecasting konsumsi energi tahunan. Untuk deteksi anomali, digunakan Isolation Forest yang mengidentifikasi gedung dengan pola konsumsi menyimpang dari profil normalnya. Model dioptimasi untuk iklim tropis dengan mengintegrasikan data cuaca Jakarta dari Open-Meteo Historical API. Output: prediksi konsumsi baseline (kWh/tahun) dan klasifikasi anomali per gedung.

3. **Rekomendasi Aksi (Prescriptive):** Membandingkan prediksi baseline dengan standar Intensitas Konsumsi Energi (IKE) Indonesia (Permen ESDM No. 13/2012). Gedung dengan IKE >145 kWh/m²/tahun terklasifikasi "boros" dan mendapat rekomendasi spesifik: penjadwalan ulang sistem pendingin, identifikasi peralatan inefisien, dan estimasi potensi penghematan dalam Rupiah. Hasil divisualisasikan pada peta interaktif dengan pin berwarna per gedung (hijau = efisien, merah = boros).

---

## Fitur Utama dan Teknologi yang Digunakan

### Fitur Utama:
- **Energy Consumption Forecasting** — Prediksi konsumsi energi tahunan per gedung menggunakan ensemble Gradient Boosting dengan log-transformed target, dioptimasi via RandomizedSearchCV (20 iterasi, 3-fold cross-validation)
- **Energy Anomaly Detection** — Deteksi otomatis pola konsumsi energi abnormal pada gedung menggunakan Isolation Forest (contamination rate 10%), menandai gedung-gedung dengan potensi kebocoran energi atau kerusakan peralatan
- **Building Clustering Analysis** — Pengelompokan gedung berdasarkan profil konsumsi energi menggunakan K-Means (5 cluster) untuk identifikasi pola dan best practices antar gedung serupa. Cluster digunakan sebagai fitur tambahan (one-hot encoded) untuk memperkuat model prediksi
- **IKE Efficiency Scoring** — Penilaian efisiensi energi per gedung berdasarkan standar Intensitas Konsumsi Energi Indonesia (kWh/m²/tahun) dengan kategori: Sangat Efisien (<50), Efisien (50-95), Cukup (95-145), Boros (145-175), Sangat Boros (>175)
- **Interactive Map Dashboard** — Peta interaktif Jakarta (Plotly Mapbox) dengan pin per gedung pemerintah, warna berdasarkan rating efisiensi, klik untuk detail dan rekomendasi AI
- **ROI Calculator** — Estimasi penghematan biaya listrik (Rupiah/tahun) pada 2 skenario: konservatif (10%) dan optimis (30%), berdasarkan tarif PLN golongan P (Rp1.400/kWh)
- **Comparative Analysis** — Benchmarking performa energi antar gedung per kategori (kantor vs pelayanan publik) dan ranking gedung dari paling boros ke paling efisien

### Teknologi yang Digunakan:

| Layer | Teknologi |
|-------|-----------|
| **Data Processing** | Python, Pandas, NumPy, Scikit-learn |
| **Machine Learning** | GradientBoostingRegressor (forecasting), Isolation Forest (anomaly detection), K-Means (clustering), RandomizedSearchCV (hyperparameter tuning) |
| **Feature Engineering** | LabelEncoder, log-transform, building age, avg floor area, type interactions, weather features, cluster one-hot encoding |
| **Azure Services** | Azure Machine Learning (training & model registry), Azure App Service (web hosting) |
| **Dashboard** | Streamlit + Plotly (scatter_mapbox, histogram, bar charts) |
| **Data Sources** | BDG2 Dataset (Kaggle, CC BY-SA 4.0), Open-Meteo Historical API (cuaca Jakarta), OpenStreetMap (lokasi gedung), PLN Statistik (konsumsi per golongan tarif) |
| **Deployment** | Azure App Service (Free Tier F1) |
| **Version Control** | GitHub |

---

## Cara Penggunaan Product

### Alur Penggunaan:

**Step 1 — Landing Page**
Pengguna (operator/manajer energi Pemda DKI Jakarta) mengakses dashboard web APBN_ai melalui browser. Header menampilkan KPI utama: jumlah gedung yang dianalisis, rata-rata IKE, jumlah gedung inefisien, dan potensi penghematan total.

**Step 2 — Peta Interaktif**
Tampil peta Jakarta dengan pin gedung pemerintah. Warna pin menunjukkan rating efisiensi energi:
- 🟢 Hijau: Sangat Efisien (IKE <50 kWh/m²/yr)
- 🔵 Biru: Efisien (IKE 50-95)
- 🟡 Kuning: Cukup (IKE 95-145)
- 🟠 Oranye: Boros (IKE 145-175)
- 🔴 Merah: Sangat Boros (IKE >175)

Ukuran pin proporsional terhadap luas bangunan (m²). Hover menampilkan nama gedung, IKE, dan kategori.

**Step 3 — Detail Gedung**
Pilih gedung via dropdown → Panel detail menampilkan:
- Rating IKE dengan badge berwarna
- Kategori gedung (kantor/pelayanan publik)
- Luas bangunan (m²)
- Prediksi konsumsi tahunan (kWh) dan estimasi bulanan
- Potensi penghematan konservatif (10%) dan optimis (30%) dalam Rupiah

**Step 4 — Analytics Dashboard**
Tab terpisah untuk:
- **IKE Distribution**: Histogram distribusi IKE seluruh gedung dengan warna per kategori
- **By Category**: Bar chart rata-rata IKE per tipe gedung, dengan jumlah gedung per kategori
- **Ranking**: Tabel 15 gedung paling boros (highest IKE) beserta detail kategori dan luas

### Akses:
- **Link Prototype:** [LINK DEPLOYED PROJECT - isi nanti]
- **GitHub:** [LINK REPO - isi nanti]

---

## Informasi Pendukung

### Dataset & Sumber Data

| Dataset | Sumber | Lisensi | Deskripsi |
|---------|--------|---------|-----------|
| Building Data Genome Project 2 | [Kaggle](https://www.kaggle.com/datasets/claytonmiller/buildingdatagenomeproject2) | CC BY-SA 4.0 | 3.053 energy meters, 1.636 gedung, data hourly 2016-2017 (~53,6 juta records). Dipublikasi di Nature Scientific Data. |
| Open-Meteo Historical Weather | [open-meteo.com](https://open-meteo.com/en/docs/historical-weather-api) | CC BY 4.0 | Data cuaca historis Jakarta (suhu, kelembapan) per jam. Gratis, tanpa API key. |
| OpenStreetMap Buildings | [overpass-turbo.eu](https://overpass-turbo.eu) | ODbL | Lokasi & metadata gedung pemerintah Jakarta (koordinat, nama, tipe). |
| PLN Statistik 2022 | [web.pln.co.id](https://web.pln.co.id) | Publik | Konsumsi listrik nasional per golongan tarif (Tabel 6). Golongan P = Gedung Kantor Pemerintah: 4.995,12 GWh nasional, 1.396,61 GWh DKI Jakarta. |
| Standar IKE Indonesia | Permen ESDM No. 13/2012 | Publik | Benchmark Intensitas Konsumsi Energi untuk bangunan ber-AC di Indonesia. |

### Referensi Ilmiah
1. Miller, C., et al. (2020). *"The Building Data Genome Project 2, energy meter data from the ASHRAE Great Energy Predictor III competition."* Scientific Data, Nature. DOI: [10.1038/s41597-020-00712-x](https://doi.org/10.1038/s41597-020-00712-x)
2. ASHRAE Great Energy Predictor III Competition Solutions — [GitHub](https://github.com/buds-lab/ashrae-great-energy-predictor-iii-solutions)
3. Handbook of Energy & Economic Statistics of Indonesia (HEESI) 2023 — Kementerian ESDM
4. PP No. 33 Tahun 2023 tentang Konservasi Energi
5. GlobalABC Indonesia Roadmap — Building Energy Efficiency for Net Zero 2060
6. Statistik PLN 2022 — PT PLN (Persero), Tabel 6: Energi Terjual per Kelompok Pelanggan

### Statistik Pendukung (Semua Bersumber)
- Konsumsi listrik gedung kantor pemerintah nasional: **4.995,12 GWh/tahun** (PLN 2022, Tabel 6)
- Konsumsi listrik gedung pemerintah DKI Jakarta: **1.396,61 GWh/tahun** = **28% total nasional** (PLN 2022, Tabel 6)
- Total penjualan listrik DKI Jakarta: **34.578,29 GWh**, gedung pemerintah = **4,04%** dari total (PLN 2022)
- Total penjualan listrik nasional: **273.761,48 GWh** (PLN 2022)
- Sektor komersial mengonsumsi **4,44%** energi final nasional (HEESI 2023, Kementerian ESDM)
- Potensi penghematan energi sektor bangunan: **10–30%** (Kementerian ESDM)
- Potensi penghematan gedung pemerintah DKI Jakarta: **139–419 GWh/tahun** = **Rp195–587 miliar/tahun** (kalkulasi dari data PLN 2022 × potensi ESDM × tarif P)
- Target pengurangan konsumsi energi bangunan: **25% pada 2030** (GlobalABC Roadmap Indonesia)
- Indonesia target **Net Zero Emission 2060** — efisiensi energi berkontribusi ~37% reduksi emisi sektor energi (NDC Indonesia)

### Hasil Model (Prototipe)

| Metrik | Nilai |
|--------|-------|
| Model | GradientBoostingRegressor (tuned via RandomizedSearchCV) |
| Best Hyperparams | learning_rate=0.04, max_depth=2, min_samples_split=6, n_estimators=439, subsample=0.77 |
| RMSE | 2.522.916 kWh |
| MAE | 1.147.091 kWh |
| R² | 0,5309 |
| Target Transform | log1p (log-transformed annual kWh) |
| Anomaly Detection | Isolation Forest, contamination=10% |
| Clustering | K-Means, k=5 cluster |

> **Catatan:** R² = 0.53 pada data BDG2 cross-sectional menunjukkan bahwa model mampu menjelaskan lebih dari separuh variasi konsumsi energi hanya dari fitur metadata gedung (tanpa data meter real-time). Ini merupakan baseline yang solid — dengan penambahan data smart meter IoT pada implementasi penuh, akurasi diproyeksikan meningkat signifikan (R² > 0.85 berdasarkan benchmark ASHRAE).

### Rencana Pengembangan Ke Depan
1. **Fase 2 (Peningkatan Model):** Migrasi ke LightGBM/XGBoost untuk performa lebih tinggi, penambahan LSTM untuk time-series forecasting, dan integrasi data smart meter real-time
2. **Fase 3 (Implementasi):** Integrasi data real-time dari smart meter IoT pada gedung-gedung pilot project, deployment full-stack di Azure ML + Azure App Service
3. **Fase 4 (Scaling):** Perluasan ke gedung komersial dan perkantoran swasta di Jabodetabek
4. **Fase 5 (Nasional):** Skalasi ke kota-kota besar lain (Surabaya, Bandung, Semarang) sebagai platform nasional monitoring energi gedung

### Tim dan Peran Anggota
| No | Nama | Peran |
|----|------|-------|
| 1 | [NAMA 1] | Project Lead & ML Engineer — Pengembangan model ML, arsitektur sistem |
| 2 | [NAMA 2] | Data Engineer — Pipeline data, EDA, feature engineering |
| 3 | [NAMA 3] | Full-Stack Developer — Dashboard web, Azure deployment |

*(Sesuaikan dengan jumlah anggota tim lo)*
