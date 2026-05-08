# UTS Pengolahan Citra Digital - Restorasi Citra 

Repositori ini dibuat untuk memenuhi tugas **Ujian Tengah Semester (UTS)** mata kuliah Pengolahan Citra Digital (Semester Genap 2025/2026). Proyek ini berfokus pada perbaikan kualitas citra (restorasi) menggunakan teknik filtering dan pengolahan spasial.

## Identitas Mahasiswa
**Nama:** Putri Nur Aulia
* **NIM:** A18.2024.00139
* **Kelompok:** A18.1601
**Dosen Pengampu:** M. Naufal, S.Tr.T, M.Kom 

## Permasalahan & Solusi
Berdasarkan lembar soal, terdapat dua kasus utama yang diselesaikan:

1. **Kasus 1: Dehazing (Citra Jalan Berkabut)** 
   - **Masalah:** Penurunan kontras dan visibilitas akibat kabut atmosfer.
   - **Solusi:** Menggunakan teknik peningkatan kontras adaptif untuk mengembalikan detail objek di kejauhan.

2. **Kasus 2: Noise Reduction (Citra Pesawat)**
   - **Masalah:** Adanya *Salt-and-Pepper Noise* (bintik hitam-putih) yang mengganggu tekstur citra.
   - **Solusi:** Implementasi **Median Filter** untuk menghilangkan noise tanpa merusak ketajaman tepi objek.

## Metrik Evaluasi
Kualitas restorasi diukur dengan membandingkan citra hasil terhadap citra referensi menggunakan:
* **PSNR (Peak Signal-to-Noise Ratio):** Untuk mengukur kualitas rekonstruksi.
  **MSE (Mean Squared Error):** Untuk menghitung rata-rata kesalahan kuadrat piksel.
