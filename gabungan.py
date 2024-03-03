import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Files to Load
file_to_load_hour = "Bike-sharing-dataset\hour.csv"
file_to_output_hour = "bike_analysis.txt"

file_to_load_day = "Bike-sharing-dataset\day.csv"
file_to_output_day = "analisis_penggunaan.txt"

# Variables to Track
total_days_hour = 0
total_bike_users_effective_hours = 0
total_bike_users_other_hours = 0

total_days_day = 0
total_users = 0
weekday_users = 0
weekend_users = 0

unique_days_hour = set()

# Read Hourly Data
with open(file_to_load_hour) as bike_data_hour:
    reader_hour = csv.DictReader(bike_data_hour)

    for row_hour in reader_hour:
        timestamp_hour = datetime.strptime(row_hour["dteday"] + " " + row_hour["hr"], "%Y-%m-%d %H")

        if 8 <= timestamp_hour.hour <= 16:
            total_bike_users_effective_hours += int(row_hour["cnt"])

        total_bike_users_other_hours += int(row_hour["cnt"])

        unique_days_hour.add(row_hour["dteday"])

    total_days_hour = len(unique_days_hour)

    with open(file_to_output_hour, "w") as txt_file_hour:
        txt_file_hour.write("Total Days: " + str(total_days_hour))
        txt_file_hour.write("\n")
        txt_file_hour.write("Total Bike Users (08:00-16:00): " + str(total_bike_users_effective_hours))
        txt_file_hour.write("\n")
        txt_file_hour.write("Total Bike Users (Other Hours): " + str(total_bike_users_other_hours))

# Read Daily Data
with open(file_to_load_day) as user_data:
    reader_day = csv.DictReader(user_data)

    for row_day in reader_day:
        total_days_day += 1
        total_users += int(row_day["cnt"])

        if int(row_day["workingday"]) == 1:
            weekday_users += int(row_day["cnt"])
        else:
            weekend_users += int(row_day["cnt"])

avg_users_per_day = total_users / total_days_day
avg_users_weekday = weekday_users / (total_days_day // 5)
avg_users_weekend = weekend_users / (total_days_day // 2)

# Show Output for Hourly Data
print("Bike Usage Analysis (Hourly Data)")
print("-------------------------")
print("Total Days: " + str(total_days_hour))
print("Total Bike Users (08:00-16:00): " + str(total_bike_users_effective_hours))
print("Total Bike Users (Other Hours): " + str(total_bike_users_other_hours))

# Output Files for Hourly Data
with open(file_to_output_hour, "a") as txt_file_hour:
    txt_file_hour.write("\n\nGraph Data:")
    txt_file_hour.write("\nDays,Effective Hours,Other Hours")
    txt_file_hour.write(f"\n{total_days_hour},{total_bike_users_effective_hours},{total_bike_users_other_hours}")

# Show Output for Daily Data
print("\nAnalisis Penggunaan (Daily Data)")
print("-------------------------")
print("Total Hari: " + str(total_days_day))
print("Total Pengguna: " + str(total_users))
print("Rata-rata Pengguna per Hari: " + str(round(avg_users_per_day, 2)))
print("Rata-rata Pengguna pada Hari Kerja: " + str(round(avg_users_weekday, 2)))
print("Rata-rata Pengguna pada Akhir Pekan: " + str(round(avg_users_weekend, 2)))

# Output Files for Daily Data
with open(file_to_output_day, "w") as txt_file_day:
    txt_file_day.write("Total Hari: " + str(total_days_day))
    txt_file_day.write("\n")
    txt_file_day.write("Total Pengguna: " + str(total_users))
    txt_file_day.write("\n")
    txt_file_day.write("Rata-rata Pengguna per Hari: " + str(round(avg_users_per_day, 2)))
    txt_file_day.write("\n")
    txt_file_day.write("Rata-rata Pengguna pada Hari Kerja: " + str(round(avg_users_weekday, 2)))
    txt_file_day.write("\n")
    txt_file_day.write("Rata-rata Pengguna pada Akhir Pekan: " + str(round(avg_users_weekend, 2)))

# Plotting
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Hourly Analysis
axes[0, 0].bar(["Effective Hours", "Other Hours"], [total_bike_users_effective_hours, total_bike_users_other_hours], color=['blue', 'orange'])
axes[0, 0].set_title("Bike Usage Analysis (Hourly Data)")
axes[0, 0].set_ylabel("Total Bike Users")
axes[0, 0].grid(True)

# Daily Analysis
axes[0, 1].bar(["Total Users", "Avg Users/Day", "Avg Users (Weekday)", "Avg Users (Weekend)"],
              [total_users, avg_users_per_day, avg_users_weekday, avg_users_weekend], color=['green', 'red', 'purple', 'brown'])
axes[0, 1].set_title("Analisis Penggunaan (Daily Data)")
axes[0, 1].set_ylabel("Count/Average")
axes[0, 1].grid(True)

# Additional Plotting
axes[1, 0].axis("off")
axes[1, 1].axis("off")

plt.tight_layout()
plt.show()
