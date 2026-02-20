import numpy as np
import matplotlib.pyplot as plt

def simulate_digitization(analog_function, sampling_rate, quantization_levels):
    """
    analog_function : fungsi kontinu f(x)
    sampling_rate : jumlah sampel per interval
    quantization_levels : jumlah level kuantisasi
    """

    print("\n===================================")
    print("      SIMULASI DIGITALISASI SINYAL")
    print("===================================")

    # 1. Membuat sinyal analog kontinu
    x_continuous = np.linspace(0, 10, 1000)
    y_continuous = analog_function(x_continuous)

    print("\n1. SINYAL ANALOG")
    print("Sinyal analog bersifat kontinu.")
    print("Memiliki nilai tak terbatas pada setiap titik.")

    # 2. Sampling
    x_sampled = np.linspace(0, 10, sampling_rate)
    y_sampled = analog_function(x_sampled)

    print("\n2. PROSES SAMPLING")
    print("Jumlah titik sampling :", sampling_rate)
    print("Sampling mengubah sinyal kontinu menjadi diskrit.")

    # 3. Quantization
    y_min = min(y_sampled)
    y_max = max(y_sampled)

    step_size = (y_max - y_min) / quantization_levels

    y_quantized = np.round((y_sampled - y_min) / step_size) * step_size + y_min

    print("\n3. PROSES QUANTIZATION")
    print("Jumlah level kuantisasi :", quantization_levels)
    print("Step size :", step_size)

    print("Quantization mengubah nilai amplitudo menjadi level tertentu.")

    # 4. Visualisasi
    plt.figure(figsize=(12,6))

    # sinyal analog
    plt.plot(x_continuous, y_continuous, label="Sinyal Analog", linewidth=2)

    # sampling
    plt.scatter(x_sampled, y_sampled, label="Sampling", marker='o')

    # quantization
    plt.step(x_sampled, y_quantized, label="Quantization")

    plt.title("Simulasi Digitalisasi: Analog vs Sampling vs Quantization")
    plt.xlabel("Waktu")
    plt.ylabel("Amplitudo")
    plt.legend()
    plt.grid()

    plt.show()

    # 5. Analisis perbandingan
    error_sampling = np.mean(np.abs(y_continuous[:sampling_rate] - y_sampled))
    error_quantization = np.mean(np.abs(y_sampled - y_quantized))

    print("\n4. ANALISIS HASIL")
    print("Error sampling :", error_sampling)
    print("Error quantization :", error_quantization)

    print("\nPenjelasan:")
    print("Sampling menghasilkan data diskrit dari sinyal kontinu.")
    print("Quantization menyebabkan kehilangan informasi karena pembulatan nilai.")
    print("Semakin tinggi sampling rate, semakin akurat hasil digital.")
    print("Semakin banyak level quantization, semakin kecil error.")

    print("\n===================================")
    print("KESIMPULAN")
    print("===================================")
    print("Digitalisasi terdiri dari dua proses utama:")
    print("1. Sampling (diskritisasi waktu)")
    print("2. Quantization (diskritisasi amplitudo)")
    print("Kualitas sinyal digital dipengaruhi oleh kedua proses tersebut.")

# contoh fungsi analog
def analog_signal(x):
    return np.sin(x)

# jalankan simulasi
simulate_digitization(
    analog_function=analog_signal,
    sampling_rate=50,
    quantization_levels=8
)
