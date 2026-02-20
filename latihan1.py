import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def analyze_my_image(image_path):
    """Analyze your own image sesuai instruksi praktikum"""

    img = cv2.imread(image_path)

    if img is None:
        print("Gambar tidak ditemukan. Pastikan path benar.")
        return

    print("\n===================================")
    print("        ANALISIS CITRA DIGITAL")
    print("===================================")

    # 1. Dimensi dan resolusi
    height, width, channels = img.shape
    total_pixels = height * width
    file_size = os.path.getsize(image_path)/1024

    print("\n1. DIMENSI DAN RESOLUSI CITRA")
    print("Lebar gambar        :", width, "piksel")
    print("Tinggi gambar       :", height, "piksel")
    print("Jumlah channel      :", channels)
    print("Total piksel        :", total_pixels)
    print("Ukuran file         :", round(file_size,2), "KB")

    print("\nPenjelasan:")
    print("Resolusi citra menunjukkan jumlah piksel penyusun gambar.")
    print("Semakin besar resolusi, semakin tinggi detail gambar.")
    print("Jumlah channel menunjukkan gambar berwarna (RGB).")

    # 2. Aspect ratio
    aspect_ratio = width / height
    print("\n2. ASPECT RATIO")
    print("Aspect ratio:", aspect_ratio)

    print("Penjelasan:")
    print("Aspect ratio adalah perbandingan lebar dan tinggi citra.")
    print("Digunakan agar gambar tidak terlihat melebar atau memanjang saat ditampilkan.")

    # 3. Konversi grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print("\n3. KONVERSI GRAYSCALE")
    print("Ukuran grayscale:", gray.shape)

    print("Penjelasan:")
    print("Grayscale mengubah citra warna menjadi abu-abu.")
    print("Digunakan untuk analisis bentuk, tekstur, dan deteksi objek.")

    # 4. Statistik citra
    mean_val = np.mean(img)
    std_val = np.std(img)
    min_val = np.min(img)
    max_val = np.max(img)

    print("\n4. STATISTIK CITRA")
    print("Mean (rata-rata intensitas) :", mean_val)
    print("Standar deviasi             :", std_val)
    print("Nilai minimum piksel        :", min_val)
    print("Nilai maksimum piksel       :", max_val)

    print("\nPenjelasan:")
    print("Mean menunjukkan tingkat kecerahan gambar.")
    print("Standar deviasi menunjukkan variasi warna.")
    print("Min dan max menunjukkan rentang intensitas piksel.")

    # Analisis pencahayaan
    if mean_val < 85:
        kondisi = "Citra cenderung gelap"
    elif mean_val > 170:
        kondisi = "Citra cenderung terang"
    else:
        kondisi = "Pencahayaan normal"

    print("\nAnalisis pencahayaan:", kondisi)

    # 5. Histogram RGB
    colors = ('b','g','r')
    plt.figure()
    for i, col in enumerate(colors):
        hist = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(hist, color=col)

    plt.title("Histogram RGB")
    plt.xlabel("Intensitas")
    plt.ylabel("Jumlah piksel")
    plt.show()

    print("\n5. HISTOGRAM RGB")
    print("Histogram menunjukkan distribusi warna merah, hijau, dan biru.")
    print("Warna dominan terlihat dari grafik yang paling tinggi.")

    # 6. Perbandingan ukuran grayscale dan RGB
    print("\n6. PERBANDINGAN RGB DAN GRAYSCALE")
    print("Ukuran RGB      :", img.shape)
    print("Ukuran grayscale:", gray.shape)

    print("Grayscale memiliki 1 channel.")
    print("RGB memiliki 3 channel warna.")

    # tampilkan gambar
    cv2.imshow("Citra Asli", img)
    cv2.imshow("Grayscale", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("\n===================================")
    print("KESIMPULAN ANALISIS")
    print("===================================")
    print("Citra memiliki resolusi", width, "x", height)
    print("Jumlah piksel:", total_pixels)
    print("Kondisi pencahayaan:", kondisi)
    print("Distribusi warna terlihat pada histogram.")
    print("Grayscale menyederhanakan informasi warna menjadi intensitas.")

# jalankan
analyze_my_image("sunset.jpeg")
