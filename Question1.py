import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
bike_sharing_dataset = fetch_ucirepo(id=275) 
  
# data (as pandas dataframes) 
X = bike_sharing_dataset.data.features 
y = bike_sharing_dataset.data.targets 
# Fetch bike sharing dataset with ID 275
bike_sharing_dataset = fetch_ucirepo(id=275)

# Check if 'hr' is available in the features
if 'hr' in bike_sharing_dataset.data.features:
    # Access 'hr' variable from the dataset
    hr_variable = bike_sharing_dataset.data.features['hr']

    # Create a DataFrame with 'hr' variable
    df_hour = pd.DataFrame(data=hr_variable, columns=['hr'])

    # Display the first few rows of the DataFrame
    print("First 5 rows of the 'hr' variable:")
    print(df_hour.head())
else:
    print("'hr' variable is not available in the features.")

if 'dteday' in bike_sharing_dataset.data.features:
    # Access 'dteday' variable from the dataset
    dteday_variable = bike_sharing_dataset.data.features['dteday']

    # Create a DataFrame with 'dteday' variable
    df_dteday = pd.DataFrame(data=dteday_variable, columns=['dteday'])

    # Display the first few rows of the DataFrame
    print("\nFirst 5 rows of the 'dteday' variable:")
    print(df_dteday.head())

    # Save the 'dteday' DataFrame to a CSV file
    dteday_file_path = 'dteday_variable.csv'
    df_dteday.to_csv(dteday_file_path, index=False)
    print(f"'dteday' variable saved to: {dteday_file_path}")
else:
    print("'dteday' variable is not available in the features.")


# Print the column names
print("\nColumn names of the DataFrame:")
print(df_hour.columns)
print(df_dteday.columns)

# Informasi day dataset
print("\nDay dataset information:")
print(df_hour.info())
print(df_dteday.info())

# Jumlah missing values dalam setiap kolom
print("\nMissing values in each column for day dataset:")
print(df_hour.isnull().sum())
print(df_dteday.isnull().sum())

# Visualisasi missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df_hour.isnull(), cmap='viridis', cbar=False)
plt.title('Missing Values Heatmap for hour dataset')
plt.show()

# Deskripsi statistik untuk kolom-kolom numerik
print("\nDescriptive statistics for numerical columns in day dataset:")
print(df_hour.describe())
print(df_dteday.describe())


# Pengecekan duplicated columns
print("\nNumber of duplicated columns in day dataset:")
print(df_hour.duplicated().sum())
print(df_dteday.duplicated().sum())


# Nilai unik dalam setiap kolom
print("\nUnique values in each column for day dataset:")
for column in df_hour.columns:
    print(f"{column}: {df_hour[column].nunique()} unique values")


# Pengisian nilai yang hilang dengan modus untuk kolom kategorikal
df_hour.fillna(df_hour.mode().iloc[0], inplace=True)

# Jumlah missing values setelah cleaning
print("\nMissing values after cleaning for day dataset:")
print(df_hour.isnull().sum())

# Menghapus duplicated columns
df_hour.drop_duplicates(inplace=True)

# Simpan data yang sudah dibersihkan
cleaned_hour_file_path = 'cleaned_hour_bike_data.csv'
df_hour.to_csv(cleaned_hour_file_path, index=False)

print(f"\nCleaned day data saved to: {cleaned_hour_file_path}")
# Print the first few columns of the DataFrame


# Variables to Track
total_days = 0
total_bike_users_effective_hours = 0
total_bike_users_other_hours = 0

# Set to keep track of unique days
unique_days = set()

# Read Files
with open(cleaned_hour_file_path) as bike_data:
    reader = csv.DictReader(bike_data)

    
    for index, row in df_dteday.iterrows():
        # Convert the time to a datetime object for easier comparison
        timestamp = datetime.strptime(str(row["dteday"]) + " " + str(df_hour.loc[index, "hr"]), "%Y-%m-%d %H")

        # Check if the timestamp is within the effective hours (08:00-16:00)
        if 8 <= timestamp.hour <= 16:
            # Calculate the totals for effective hours
            total_bike_users_effective_hours += df_hour[column].sum()

        # Calculate the totals for other hours
        total_bike_users_other_hours += df_hour[column].sum()

        # Keep track of unique days
        unique_days.add(row["dteday"])  # Assuming 'dteday' is a static value for each row

    # Calculate the total number of unique days
    total_days = len(unique_days)
    total_user = (total_bike_users_effective_hours+total_bike_users_other_hours)

    # Show Output
    print()
    print()
    print("Bike Usage Analysis")
    print("-------------------------")
    print("Total Days: " + str(total_days))
    print("Total Bike Users (08:00-16:00): " + str(total_bike_users_effective_hours))
    print("Total Bike Users (Other Hours): " + str(total_bike_users_other_hours))



# Output Files
with open(cleaned_hour_file_path, "w") as txt_file:  # Changed file_to_output to cleaned_hour_file_path
    txt_file.write("Total Days: " + str(total_days))
    txt_file.write("\n")
    txt_file.write("Total Bike Users (08:00-16:00): " + str(total_bike_users_effective_hours))
    txt_file.write("\n")
    txt_file.write("Total Bike Users (Other Hours): " + str(total_bike_users_other_hours))
  
