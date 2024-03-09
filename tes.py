# Dependencies
import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Files to Load
file_to_load = "Bike-sharing-dataset\day.csv"
file_to_output = "bike_analysis.txt"

# Baca data ke dalam DataFrame

file_path = 'Bike-sharing-dataset\day.csv'
df = pd.read_csv('Bike-sharing-dataset\day.csv', sep=',')

# Tampilkan 5 baris pertama dari dataset
print("First 5 rows of the dataset:")
print(df.head())

# Informasi dataset
print("\nDataset information:")
print(df.info())

# Jumlah missing values dalam setiap kolom
print("\nMissing values in each column:")
print(df.isnull().sum())

# Visualisasi missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cmap='viridis', cbar=False)
plt.title('Missing Values Heatmap')
plt.show()

# Deskripsi statistik untuk kolom-kolom numerik
print("\nDescriptive statistics for numerical columns:")
print(df.describe())

# Deskripsi statistik untuk kolom-kolom kategorikal
print("\nDescriptive statistics for categorical columns:")
print(df.describe(include='object'))

# Pengecekan duplicated rows
print("\nNumber of duplicated rows:")
print(df.duplicated().sum())

# Nilai unik dalam setiap kolom
print("\nUnique values in each column:")
for column in df.columns:
    print(f"{column}: {df[column].nunique()} unique values")

# Pengisian nilai yang hilang dengan mean untuk kolom numerik
df.fillna(df.mean(), inplace=True)

# Pengisian nilai yang hilang dengan modus untuk kolom kategorikal
df.fillna(df.mode().iloc[0], inplace=True)


# Jumlah missing values setelah cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Menghapus duplicated rows
df.drop_duplicates(inplace=True)

# Simpan data yang sudah dibersihkan
cleaned_file_path = 'cleaned_bike_data.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned data saved to: {cleaned_file_path}")
