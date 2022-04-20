# -*- coding: utf-8 -*-
"""UAS_INFLing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y27snLH5pULwH9A5-DIm9J25bLqbYRVm
"""

#Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Import Gdrive
from google.colab import drive
drive.mount('/content/drive')
import warnings
warnings.filterwarnings("ignore")

"""# Membaca dataframe (xlsx) kelompok masing-masing dan mengubahnya ke csv"""

df = pd.read_csv('/content/drive/MyDrive/dataset_bmkg.csv')
df

df.isnull().sum().sum()

"""#  Mengenali outliers untuk kesepuluh fitur dan menggantinya dengan NaN"""

# periksa baris-baris curah hujan yang mengandung outliers
for n in range (0, 978):
  # jika lebih dari kondisi maka ubah value menjadi NaN
  if df.at[n, 'Curah Hujan'] > 120:
    df.at[n, 'Curah Hujan'] = np.nan

# periksa baris-baris kelembaban yang mengandung outliers
for n in range (0, 978):
  # jika lebih dari kondisi maka ubah value menjadi NaN
  if df.at[n, 'Kelembaban'] > 100:
    df.at[n, 'Kelembaban'] = np.nan

# periksa baris-baris Lamanya Penyinaran yang mengandung outliers
for n in range (0, 978):
  # jika lebih dari kondisi maka ubah value menjadi NaN
  if df.at[n, 'Lamanya Penyinaran'] > 12:
    df.at[n, 'Lamanya Penyinaran'] = np.nan

df['Temp Maks'] = df['Temp Maks'].astype(float)
# periksa baris-baris Temp Maks yang mengandung outliers
for n in range (0, 978):
  # jika lebih dari kondisi maka ubah value menjadi NaN
  if df.at[n, 'Temp Maks'] > 45:
    df.at[n, 'Temp Maks'] = np.nan

df['Temp Min'] = df['Temp Min'].astype(float)
# periksa baris-baris Temp Min yang mengandung outliers
for n in range (0, 978):
  # jika lebih dari kondisi maka ubah value menjadi NaN
  if df.at[n, 'Temp Min'] < 15:
    df.at[n, 'Temp Min'] = np.nan

df

"""# Mengenali baris yang mengandung data NaN dan menghapus baris tersebut"""

# Mengenali baris yang mengandung data NaN
df.isnull()

df.isnull().sum().sum()

# Menghapus baris yang mengandung NaN
df = df.dropna()
df

df.isnull().sum().sum()

df.loc[df['Curah Hujan'] == 8888.0]

"""# Data sudah selesai dibersihkan
Selanjutnya kita akan menambahkan kolom Curah Hujan (d+1) yang berisikan value dari kolom hujan dimulai dari baris kedua
"""

for n in range(0, 543):
  df.loc[df.index[n], 'Curah Hujan (d+1)'] = df.loc[df.index[n+1], 'Curah Hujan'] 

#df.loc[df.index[529], 'Curah Hujan (d+1)'] = np.nan
df

"""# Membagi dataset menjadi dua


*   dfLatih = Dataset latihan berisi 519 Baris
*   dfUji = Dataset uji berisi 10 Baris


"""

# Menaruh nilai df ke dalam dataframe bernama dfLatih
dfLatih = df
dfLatih

# Menentukan nilai max dan min Kelembaban
columnKelembaban = dfLatih['Kelembaban']
maxValueKelembaban = columnKelembaban.max()
print (maxValueKelembaban)

columnKelembaban = dfLatih['Kelembaban']
minValueKelembaban = columnKelembaban.min()
print (minValueKelembaban)

# Menentukan nilai max dan min Lama Penyinaran
columnLama = dfLatih['Lamanya Penyinaran']
maxValueLama = columnLama.max()
print (maxValueLama)

columnLama = dfLatih['Lamanya Penyinaran']
minValueLama = columnLama.min()
print (minValueLama)

# Menentukan nilai max dan min Temperatur Maksimal
columnTempMaks = dfLatih['Temp Maks']
maxValueTempMaks = columnTempMaks.max()
print (maxValueTempMaks)

columnTempMaks = dfLatih['Temp Maks']
minValueTempMaks = columnTempMaks.min()
print (minValueTempMaks)

# Menentukan nilai max dan min Temperatur Minimal
columnTempMin = dfLatih['Temp Min']
maxValueTempMin = columnTempMin.max()
print (maxValueTempMin)

columnTempMin = dfLatih['Temp Min']
minValueTempMin = columnTempMin.min()
print (minValueTempMin)

# Menentukan nilai max dan min Curah Hujan
columnCurahHujan = dfLatih['Curah Hujan']
maxValueCurahHujan = columnCurahHujan.max()
print (maxValueCurahHujan)

columnCurahHujan = dfLatih['Curah Hujan']
minValueCurahHujan = columnCurahHujan.min()
print (minValueCurahHujan)

# Menentukan nilai max dan min Curah Hujan (d+1)
columnBesok = dfLatih['Curah Hujan (d+1)']
maxValueBesok = columnBesok.max()
print (maxValueBesok)

columnBesok = dfLatih['Curah Hujan (d+1)']
minValueBesok = columnBesok.min()
print (minValueBesok)

"""# Melakukan normalisasi terhadap nilai di dalam dataframe dfLatih"""

for n in range(0, 543):
  dfLatih.loc[df.index[n], 'Kelembaban'] = ((dfLatih.loc[df.index[n], 'Kelembaban'])-minValueKelembaban)/(maxValueKelembaban-minValueKelembaban)
  dfLatih.loc[df.index[n], 'Lamanya Penyinaran'] = ((dfLatih.loc[df.index[n], 'Lamanya Penyinaran'])-minValueLama)/(maxValueLama-minValueLama)
  dfLatih.loc[df.index[n], 'Temp Maks'] = ((dfLatih.loc[df.index[n], 'Temp Maks'])-minValueTempMaks)/(maxValueTempMaks-minValueTempMaks)
  dfLatih.loc[df.index[n], 'Temp Min'] = ((dfLatih.loc[df.index[n], 'Temp Min'])-minValueTempMin)/(maxValueTempMin-minValueTempMin)
  dfLatih.loc[df.index[n], 'Curah Hujan'] = ((dfLatih.loc[df.index[n], 'Curah Hujan'])-minValueCurahHujan)/(maxValueCurahHujan-minValueCurahHujan)
  dfLatih.loc[df.index[n], 'Curah Hujan (d+1)'] = ((dfLatih.loc[df.index[n], 'Curah Hujan (d+1)'])-minValueBesok)/(maxValueBesok-minValueBesok)

dfLatih

"""# Dataframe latihan hanya berisikan 519 baris saja"""

# Mengambil hanya 519 baris ke dataframe dfLatih untuk dijadikan dataset latih
dfLatih = df.iloc[0:519]
dfLatih

# Mengambil hanya 10 baris ke dataframe dfUji untuk dijadikan dataset Uji
dfUji = df.iloc[520:530] # dari baris ke 520 sampai 530
dfUji

"""# Menerapkan Algoritma K-NN"""

# Melakukan import untuk library yang diperlukan
import math
import statistics

# disini akan dilakukan loop bersarang untuk mencari nilai Euclidean Distance tiap data uji lalu melanjutkannya dengan menentukan nilai prediksi tiap baris dari data uji
for n in range(0, 10): # Melakukan looping untuk tiap baris dari data uji
  barisUji = dfUji.iloc[n]
  for x in range(0, 519): # Melakukan looping untuk tiap baris dari data latihan
    barisLatih = dfLatih.iloc[x]
    # Menambahkan kolom Euclidean Distance lalu Memasukkan nilai yang berisikan rumus Euclidean Distance ke dalam looping
    # Antara dua input dari 5 kolom
    # a = baris dari data uji
    # b = baris dari data latih
    # Akar (((a1 - b1)**2) - ((a2 - b2)**2) - ((a3 - b3)**2) - ((a4 - b4)**2) - ((a5 - b5)**2))
    dfLatih.loc[dfLatih.index[x], 'Euclidean Distance'] = math.sqrt(((barisUji["Kelembaban"]-barisLatih["Kelembaban"])**2) + ((barisUji["Lamanya Penyinaran"]-barisLatih["Lamanya Penyinaran"])**2) + ((barisUji["Temp Maks"]-barisLatih["Temp Maks"])**2) + ((barisUji["Temp Min"]-barisLatih["Temp Min"])**2) + ((barisUji["Curah Hujan"]-barisLatih["Curah Hujan"])**2))
  
  # Melakukan print terhadap 10 data latih yang sekarang telah memiliki kolom Euclidean Distance
  print (dfLatih)

  # Mencari 5 baris yang memiliki nilai terkecil di kolom Euclidean Distance
  kolomDistance = dfLatih.nsmallest(5, 'Euclidean Distance')
  # Mengambil nilai pada kolom Curah Hujan (d+1) yang memiliki nilai Euclidean Distance terkecil lalu menaruhnya di variabel k5
  k5 = kolomDistance["Curah Hujan (d+1)"]
  # Mencari rata-rata dari k=5
  average = statistics.mean(k5)
  # Menambahkan kolom Prediksi Curah Hujan (d+1) dan memasukkan nilai rata-rata dari k=5 dari tiap baris data yang diuji
  dfUji.loc[dfUji.index[n], 'Prediksi Curah Hujan (d+1)'] = average

# Memanggil data uji telah memiliki kolom Prediksi Curah Hujan (d+1)
dfUji

"""# Hitung RMSE"""

# Mencari RMSE

for n in range(0, 10): # Melakukan looping sebanyak data uji
  # Menambahkan kolom RMSE dan memasukkan nilai yang berisikan rumus mencari RMSE dari nilai riil dan nilai prediksi
  # (Nilai Riil - Nilai prediksi)**2
  dfUji.loc[dfUji.index[n], 'RMSE'] = ((df.loc[dfUji.index[n], 'Curah Hujan (d+1)']) - (dfUji.loc[dfUji.index[n], 'Prediksi Curah Hujan (d+1)']))**2

dfUji

# Mencari nilai RMSE dengan mencari nilai rata-rata dari kolom RMSE dari dfUji
RMSE = dfUji['RMSE'].mean()
# Menampilkan nilai RMSE
print(f'RMSE : {RMSE}')

# Membuat variabel bykData untuk mengetahui berapa banyak row yang terdapat di dalam data uji
bykData = len(dfUji.index)
# Membuat array jmlUji untuk menampung nilai looping
jmlUji = []
for n in range(bykData): # Melakukan looping
  jmlUji.append(n) # Menambah n ke dalam array jmlUji

# Visualisasikan data riil dan data hasil dari metode K-NN
plt.plot(jmlUji, dfUji['Curah Hujan (d+1)'])
plt.plot(jmlUji, dfUji['Prediksi Curah Hujan (d+1)'])
plt.legend(['Curah Hujan (d+1) Riil', 'Prediksi Curah Hujan (d+1) K-NN'])
plt.xticks(rotation = 'vertical')
plt.show()

"""# Melakukan Denormalisasi pada kolom Prediksi Curah Hujan (d+1)"""

# Menentukan nilai max dan min Prediksi Curah Hujan (d+1)
columnPrediksi = dfUji['Prediksi Curah Hujan (d+1)']
maxValuePrediksi = columnPrediksi.max()
print (maxValuePrediksi)

columnPrediksi = dfUji['Prediksi Curah Hujan (d+1)']
minValuePrediksi = columnPrediksi.min()
print (minValuePrediksi)

for n in range(0, 10): # Melakukan looping sebanyak data uji
  # Melakukan denormalisasi pada kolom Prediksi Curah Hujan (d+1)
  # y = min + ynorm * (max - min)
  dfUji.loc[dfUji.index[n], 'Prediksi Curah Hujan (d+1)'] = (minValuePrediksi + (dfUji.loc[dfUji.index[n], 'Prediksi Curah Hujan (d+1)']) * (maxValuePrediksi - minValuePrediksi))

print ("Denormalisasi Prediksi Curah Hujan (d+1):")
print (dfUji['Prediksi Curah Hujan (d+1)'])

