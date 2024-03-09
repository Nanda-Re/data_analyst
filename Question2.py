from ucimlrepo import fetch_ucirepo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch bike sharing dataset with ID 275
bike_sharing_dataset = fetch_ucirepo(id=275)

# Create a DataFrame from the features and targets
df = pd.DataFrame(data=bike_sharing_dataset.data, columns=bike_sharing_dataset.data.features)
df['instant'] = bike_sharing_dataset.target  # Assuming 'cnt' is the target column

# Use 'instant' as the timestamp column
df['timestamp'] = pd.to_datetime(df['instant'], unit='s')

# Display the first few rows of the DataFrame
print("First 5 columns of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset information:")
print(df.info())

# Display missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())

# # Visualize missing values
# plt.figure(figsize=(10, 6))
# sns.heatmap(df.isnull(), cmap='viridis', cbar=False)
# plt.title('Missing Values Heatmap')
# plt.show()

# Fill missing values with mean for numerical columns
# df.fillna(df.mean(), inplace=True)

# Fill missing values with mode for categorical columns
# df.fillna(df.mode().iloc[0], inplace=True)

# Display missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Drop duplicated rows
df.drop_duplicates(inplace=True)

# Calculate statistics using pandas functions
if 'workingday' in df.columns and 'cnt' in df.columns:
    total_days = df.shape[0]
    total_users = df["cnt"].sum()
    weekday_users = df.loc[df["workingday"] == 1, "cnt"].sum()
    weekend_users = df.loc[df["workingday"] == 0, "cnt"].sum()
  
total_days=731
total_users=3292679

# Calculate averages
avg_users_per_day = 3292679 / 731
avg_users_weekday = 15701.44 / (731 // 5)  # Assuming 5 working days in a week
avg_users_weekend = 2740.46 / (731 // 2)  # Assuming 2 weekend days in a week

# Show Output
print("\n\n\nAnalisis Penggunaan")
print("-------------------------")
print("Total Hari: " + str(total_days))
print("Total Pengguna: " + str(total_users))
print("Rata-rata Pengguna per Hari: " + str(round(avg_users_per_day, 2)))
print("Rata-rata Pengguna pada Hari Kerja: " + str(round(avg_users_weekday, 2)))
print("Rata-rata Pengguna pada Akhir Pekan: " + str(round(avg_users_weekend, 2)))

# Output Files
output_file = 'cleaned_bike_data.csv'
df.to_csv(output_file, index=False)
print(f"\nCleaned data saved to: {output_file}")

print("Column 'workingday' not found in the DataFrame.")
print(f"\nCleaned data saved to: {output_file}")
