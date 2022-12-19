import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Grafik Jumlah Siswa kelas 12 

subjects = ['IPA 1', 'IPA 2', 'IPA 3', 'IPA 4', 'IPS 1', 'IPS2']
y = [ 30, 32, 34, 34, 28, 28 ]
x = [70, 60, 50, 40, 30, 20, 10]

plt.plot(subjects, y, color='blue',marker='o', label='siswa')
plt.title("Grafik Jumlah Siswa Kelas 12")
plt.xlabel("Kelas")
plt.ylabel("Jumlah Siswa")
plt.legend()
plt.grid()
plt.show()