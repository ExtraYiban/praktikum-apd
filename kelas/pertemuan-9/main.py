import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.figure(figsize=(12,6))

# info tambahan pada kanvas
plt.xlabel('kasih nama Sumbu X')
plt.ylabel('kasih nama Sumbu Y')
plt.title("Ini judul loh")

x = [1, 2, 3, 4, 5]
y = [10, 35, 20, 70, 60]

plt.figure(figsize=(8, 4))
# plt.plot()
plt.plot(x, y)
# Detail element
plt.title("Contoh Grafik")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.grid(True)
plt.show()