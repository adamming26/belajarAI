Deskripsi projek

# 🌦️ Analisis Cuaca Sulawesi Tenggara & Prediksi Hujan
# By Kelompok 6
👥 Anggota Kelompok 6

- Masyithah (F1G125061)
- Adam Muzakkir Eni (F1G125001)
- Muhammad Fajri Jumadil (F1G125041)

Proyek ini membangun model *supervised binary classification* untuk memprediksi
hujan atau tidak hujan berdasarkan data cuaca harian Sulawesi Tenggara.
Model dilatih menggunakan data BMKG periode 2022–2023 dan diintegrasikan
ke dalam aplikasi web interaktif berbasis Streamlit.


## Latar Belakang

Sulawesi Tenggara termasuk wilayah tropis dengan curah hujan tinggi dan tidak menentu. Perubahan iklim membuat pola hujan makin sulit diprediksi, sehingga petani, nelayan, dan masyarakat umum sering salah mengambil keputusan — mulai dari waktu tanam, waktu melaut, hingga kesiapan menghadapi cuaca ekstrem.

Proyek ini mendukung **SDGS 13: Penanganan Perubahan Iklim**, ) Model ini bukan solusi langsung untuk menghentikan perubahan iklim, melainkan alat bantu kesiapsiagaan berbasis data.

Sebagai solusi, proyek ini membangun model machine learning yang memprediksi hujan atau tidak hujan berdasarkan data cuaca harian, lalu diintegrasikan ke aplikasi web interaktif agar siapa pun bisa menggunakannya dengan mudah.

## 📊 Dataset

- **Sumber:** [Data Cuaca Harian – Kaggle](https://www.kaggle.com/datasets/ratnasarii/data-cuaca-harian) (BMKG)
- **Periode:** 1 Januari 2022 – 30 November 2023
- **Jumlah:** 699 baris, 8 kolom
- **Fitur (6):**
  - Temperatur minimum (°C)
  - Temperatur maximum (°C)
  - Temperatur rata-rata (°C)
  - Kelembapan rata-rata (%)
  - Lamanya penyinaran matahari (jam)
  - Kecepatan angin rata-rata (m/s)

## ⚙️ Metode

Proyek ini dilakukan melalui beberapa tahapan, yaitu:

1. **Pengumpulan Data**  
   Menggunakan dataset cuaca harian Sulawesi Tenggara periode 1 Januari 2022 hingga November 2023.

2. **Preprocessing Data**  
   Melakukan pemeriksaan dan pembersihan data, seperti menangani nilai kosong, memperbaiki format data, serta menyesuaikan nilai yang tidak valid agar dataset siap digunakan.

3. **Eksplorasi Data**  
   Menganalisis karakteristik dataset melalui statistik deskriptif dan visualisasi untuk memahami pola serta hubungan antarvariabel cuaca.

4. **Persiapan Data**  
   Menentukan fitur yang digunakan sebagai variabel input dan mengelompokkan kondisi cuaca menjadi dua kategori, yaitu hujan dan tidak hujan.

5. **Pemodelan Machine Learning**  
   Melatih model klasifikasi menggunakan data cuaca yang telah diproses untuk mempelajari pola yang berkaitan dengan kejadian hujan.

6. **Evaluasi Model**  
   Mengukur kinerja model menggunakan metrik evaluasi klasifikasi untuk mengetahui kemampuan model dalam memprediksi kondisi hujan dan tidak hujan.

7. **Prediksi**  
   Menggunakan model yang telah dilatih untuk memprediksi kemungkinan kondisi hujan berdasarkan data parameter cuaca yang diberikan.

## 📈 Hasil

| Model | Accuracy | F1 (Hujan) | ROC-AUC |
|---|---|---|---|
| Dummy Classifier | 0.57 | 0.73 | – |
| Logistic Regression | 0.78 | 0.82 | 0.83 |
| Random Forest | 0.80 | 0.84 | 0.81 |

**Model terbaik:** Random Forest — accuracy 0.80, recall kelas hujan 0.89
(berhasil mendeteksi 62 dari 70 hari hujan pada data uji).

### Interpretasi

Random Forest dipilih sebagai model utama karena memiliki accuracy, precision,
recall, dan F1 tertinggi. Model ini berhasil mendeteksi sebagian besar hari
hujan (recall 0.89), meskipun masih ada 16 alarm palsu (false positive).

Logistic Regression menjadi pembanding yang baik dengan ROC-AUC sedikit lebih
tinggi (0.83), namun performa keseluruhannya di bawah Random Forest.

## 📁 Struktur Repository

```text
.
├── app
│   └── app.py
├── data
│   ├── raw
│   │   └── Data Cuaca Harian SulawesiTenggara.xlsx
│   └── processed
│       ├── cuaca_sultra_clean.csv
│       └── model_prediksi_hujan.pkl
├── notebooks
│   └── olah_dataset.ipynb
├── README.md
└── requirements.txt
```
## 🛠️ Tools & Library
Proyek ini menggunakan beberapa tools dan library untuk mendukung proses pengolahan data, analisis, pemodelan machine learning, hingga pengembangan aplikasi prediksi. Setiap tools memiliki fungsi yang berbeda dan saling melengkapi dalam membangun sistem prediksi cuaca.

| Tools / Library | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| Jupyter Notebook | Pengolahan dan analisis dataset |
| Pandas | Membaca dan mengolah data |
| NumPy | Operasi numerik dan penanganan nilai |
| Matplotlib | Membuat visualisasi data |
| Scikit-learn | Training dan evaluasi model machine learning |
| Random Forest | Algoritma klasifikasi prediksi hujan |
| Joblib | Menyimpan dan memuat model |
| Streamlit | Membangun aplikasi prediksi berbasis web |

🚀 Cara Menjalankan

1. Clone repo:
   git clone https://github.com/Syifah15/dataset-project.git
   cd dataset-project

2. Install library:
   pip install -r requirements.txt

3. Jalankan aplikasi:
   python -m streamlit run app/app.py
