import cv2
import numpy as np
import math

def calculate_psnr(img1, img2):
    """Menghitung Peak Signal-to-Noise Ratio (PSNR) antara dua citra[cite: 41, 42]."""
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

# ==========================================
# KASUS 1: DEHAZING (Sederhana)
# ==========================================
def simple_dehaze(img):
    """
    Menerapkan perbaikan kontras sederhana untuk mengurangi efek kabut.
    Dapat dikembangkan menggunakan Dark Channel Prior.
    """
    # Menggunakan CLAHE (Contrast Limited Adaptive Histogram Equalization)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

# ==========================================
# KASUS 2: MEDIAN FILTER (Salt-and-Pepper)
# ==========================================
def remove_salt_pepper(img):
    """Menerapkan Median Filter untuk mereduksi noise impulsif."""
    # Kernel 3x3 atau 5x5 efektif untuk noise jenis ini
    return cv2.medianBlur(img, 3)

# --- EKSEKUSI PROGRAM ---

# Load Citra (Pastikan file ada di direktori yang sama)
img1_noisy = cv2.imread('jalan_noisy.jpg')
img1_ref = cv2.imread('jalan_reference.jpg')

img2_noisy = cv2.imread('pesawat_noisy.jpg')
img2_ref = cv2.imread('pesawat_reference.jpg')

# Proses Perbaikan [cite: 27]
result1 = simple_dehaze(img1_noisy)
result2 = remove_salt_pepper(img2_noisy)

# Evaluasi 
psnr_kasus1 = calculate_psnr(img1_ref, result1)
psnr_kasus2 = calculate_psnr(img2_ref, result2)

print(f"Hasil Evaluasi PSNR Kasus 1: {psnr_kasus1:.2f} dB")
print(f"Hasil Evaluasi PSNR Kasus 2: {psnr_kasus2:.2f} dB")

# Tampilkan Hasil
cv2.imshow('Hasil Kasus 1 (Dehaze)', result1)
cv2.imshow('Hasil Kasus 2 (Median)', result2)
cv2.waitKey(0)
cv2.destroyAllWindows()