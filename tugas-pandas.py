import pandas as pd
from collections import defaultdict

#1

df_data_sampah = pd.read_csv("jumlahsampah.csv", usecols=['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun'])
df_data_sampah.dropna(inplace=True)
print(df_data_sampah)

print("")
#2

jumlah_sampah_2015 = []
for index, row in df_data_sampah.iterrows():
    if row['tahun'] == 2015:
        jumlah_sampah_2015.append(row['jumlah_produksi_sampah'])

print(round(sum(jumlah_sampah_2015)))

print("")
#3

jumlah_sampah_pertahun = defaultdict(int)

for index, row in df_data_sampah.iterrows():
    jumlah_sampah_pertahun[row['tahun']] += row['jumlah_produksi_sampah']

jumlah_sampah_pertahun = dict(jumlah_sampah_pertahun)

for index, row in jumlah_sampah_pertahun.items():
    print(f"Total Sampah di Tahun {index}: {round(row, 2)} ")

df_jumlah_pertahun = pd.DataFrame(list(jumlah_sampah_pertahun.items()), columns=['tahun', 'total_sampah'])
df_jumlah_pertahun.to_csv('jumlah_sampah_pertahun.csv', index=False)
df_jumlah_pertahun.to_excel('jumlah_sampah_pertahun.xlsx', index=False)

print("")
#4

jumlah_sampah_perkota = defaultdict(int)

for index, row in df_data_sampah.iterrows():
    jumlah_sampah_perkota[row['nama_kabupaten_kota']] += row['jumlah_produksi_sampah']

jumlah_sampah_perkota = dict(jumlah_sampah_perkota)
for index, row in jumlah_sampah_perkota.items():
    print(f"Total sampah di {index} periode 2015-2021: {round(row, 2)}")

df_jumlah_perkota = pd.DataFrame(list(jumlah_sampah_perkota.items()), columns=['wilayah', 'total_sampah'])
df_jumlah_perkota.to_csv('sampah_perkota.csv', index=False)
df_jumlah_perkota.to_excel('sampah_perkota.xlsx', index=False)

for index, row in df_data_sampah.iterrows():
    print(f"Total sampah di {row['nama_kabupaten_kota']} pada {row['tahun']}: {row['jumlah_produksi_sampah']}")