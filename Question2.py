# Dependencies
import csv

# Files to Load
file_to_load = "Bike-sharing-dataset\day.csv"  # Ganti dengan nama file CSV yang sesuai
file_to_output = "analisis_penggunaan.txt"

# Variables to Track
total_days = 0
total_users = 0

weekday_users = 0
weekend_users = 0

# Read Files
with open(file_to_load) as user_data:
    reader = csv.DictReader(user_data)

    # Loop through all the rows of data
    for row in reader:

        # Calculate the totals
        total_days += 1
        total_users += int(row["cnt"])

        # Categorize users based on weekdays and weekends
        if int(row["workingday"]) == 1:  # 1 represents a working day
            weekday_users += int(row["cnt"])
        else:
            weekend_users += int(row["cnt"])

# Calculate averages
avg_users_per_day = total_users / total_days
avg_users_weekday = weekday_users / (total_days // 5)  # Assuming 5 working days in a week
avg_users_weekend = weekend_users / (total_days // 2)  # Assuming 2 weekend days in a week

# Show Output
print()
print()
print()
print("Analisis Penggunaan")
print("-------------------------")
print("Total Hari: " + str(total_days))
print("Total Pengguna: " + str(total_users))
print("Rata-rata Pengguna per Hari: " + str(round(avg_users_per_day, 2)))
print("Rata-rata Pengguna pada Hari Kerja: " + str(round(avg_users_weekday, 2)))
print("Rata-rata Pengguna pada Akhir Pekan: " + str(round(avg_users_weekend, 2)))

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Hari: " + str(total_days))
    txt_file.write("\n")
    txt_file.write("Total Pengguna: " + str(total_users))
    txt_file.write("\n")
    txt_file.write("Rata-rata Pengguna per Hari: " + str(round(avg_users_per_day, 2)))
    txt_file.write("\n")
    txt_file.write("Rata-rata Pengguna pada Hari Kerja: " + str(round(avg_users_weekday, 2)))
    txt_file.write("\n")
    txt_file.write("Rata-rata Pengguna pada Akhir Pekan: " + str(round(avg_users_weekend, 2)))
