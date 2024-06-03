import time
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 4 / (1 + x**2)

def trapezoid(a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    
    for i in range(1, n):
        integral += f(a + i * h)
    
    integral *= h
    return integral

# Batas integral
a = 0
b = 1

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi N (jumlah segmen)
N_values = [10, 100, 1000, 10000]

# Menyimpan hasil
results = []

for n in N_values:
    start_time = time.time()
    pi_approx = trapezoid(a, b, n)
    end_time = time.time()
    
    # Menghitung galat RMS
    rms_error = np.sqrt((pi_approx - pi_reference)**2)
    
    # Mengukur waktu eksekusi
    execution_time = end_time - start_time
    
    results.append((n, pi_approx, rms_error, execution_time))

# Menampilkan hasil
print(f"{'N':>10} {'Pi Approximation':>20} {'RMS Error':>20} {'Execution Time (s)':>20}")
for result in results: 
    print(f"{result[0]:>10} {result[1]:>20.15f} {result[2]:>20.15f} {result[3]:>20.15f}")

# Pisahkan hasil ke dalam array terpisah
N_array = np.array([result[0] for result in results])
pi_approx_array = np.array([result[1] for result in results])
rms_error_array = np.array([result[2] for result in results])
execution_time_array = np.array([result[3] for result in results])

# Membuat plot
plt.figure(figsize=(14, 6))

# Plot galat RMS
plt.subplot(1, 2, 1)
plt.plot(N_array, rms_error_array, 'o-', color='blue')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (Jumlah Segmen)')
plt.ylabel('RMS Error')
plt.title('RMS Error vs Jumlah Segmen')
plt.grid(True)

# Plot waktu eksekusi
plt.subplot(1, 2, 2)
plt.plot(N_array, execution_time_array, 'o-', color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (Jumlah Segmen)')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs Jumlah Segmen')
plt.grid(True)

# Tampilkan plot
plt.tight_layout()
plt.show()
