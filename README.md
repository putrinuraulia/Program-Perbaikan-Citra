# UTS Pengolahan Citra Digital - Restorasi Citra 📸

Repositori ini dibuat untuk memenuhi tugas **Ujian Tengah Semester (UTS)** mata kuliah Pengolahan Citra Digital (Semester Genap 2025/2026). Proyek ini berfokus pada perbaikan kualitas citra (restorasi) menggunakan teknik filtering dan pengolahan spasial.

## 👤 Identitas Mahasiswa
* [cite_start]**Nama:** Putri Nur Aulia [cite: 45]
* **NIM:** A18.2024.00139
* [cite_start]**Kelompok:** A18.1601 [cite: 17]
* [cite_start]**Dosen Pengampu:** M. Naufal, S.Tr.T, M.Kom [cite: 18, 45]

## 🛠️ Permasalahan & Solusi
[cite_start]Berdasarkan lembar soal[cite: 10], terdapat dua kasus utama yang diselesaikan:

1. [cite_start]**Kasus 1: Dehazing (Citra Jalan Berkabut)** [cite: 31, 33]
   - **Masalah:** Penurunan kontras dan visibilitas akibat kabut atmosfer.
   - **Solusi:** Menggunakan teknik peningkatan kontras adaptif untuk mengembalikan detail objek di kejauhan.

2. [cite_start]**Kasus 2: Noise Reduction (Citra Pesawat)** [cite: 32, 33]
   - **Masalah:** Adanya *Salt-and-Pepper Noise* (bintik hitam-putih) yang mengganggu tekstur citra.
   - [cite_start]**Solusi:** Implementasi **Median Filter** untuk menghilangkan noise tanpa merusak ketajaman tepi objek[cite: 22].

## 📊 Metrik Evaluasi
[cite_start]Kualitas restorasi diukur dengan membandingkan citra hasil terhadap citra referensi [cite: 34] menggunakan:
* **PSNR (Peak Signal-to-Noise Ratio):** Untuk mengukur kualitas rekonstruksi.
* [cite_start]**MSE (Mean Squared Error):** Untuk menghitung rata-rata kesalahan kuadrat piksel[cite: 41].

## 🚀 Cara Menjalankan Program
1. Pastikan Anda memiliki Python terinstal.
2. Install library yang dibutuhkan:
   ```bash
   pip install opencv-python numpy
