# Dependencies
import csv
from datetime import datetime

# Files to Load
file_to_load = "Bike-sharing-dataset\hour.csv"
file_to_output = "bike_analysis.txt"

# Variables to Track
total_days = 0
total_bike_users_effective_hours = 0
total_bike_users_other_hours = 0

# Set to keep track of unique days
unique_days = set()

# Read Files
with open(file_to_load) as bike_data:
    reader = csv.DictReader(bike_data)

    # Loop through all the rows of data we collect
    for row in reader:
        # Convert the time to a datetime object for easier comparison
        timestamp = datetime.strptime(row["dteday"] + " " + row["hr"], "%Y-%m-%d %H")

        # Check if the timestamp is within the effective hours (08:00-16:00)
        if 8 <= timestamp.hour <= 16:
            # Calculate the totals for effective hours
            total_bike_users_effective_hours += int(row["cnt"])

        # Calculate the totals for other hours
        total_bike_users_other_hours += int(row["cnt"])

        # Keep track of unique days
        unique_days.add(row["dteday"])

    # Calculate the total number of unique days
    total_days = len(unique_days)

    # Show Output
    print()
    print()
    print("Bike Usage Analysis")
    print("-------------------------")
    print("Total Days: " + str(total_days))
    print("Total Bike Users (08:00-16:00): " + str(total_bike_users_effective_hours))
    print("Total Bike Users (Other Hours): " + str(total_bike_users_other_hours))

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Days: " + str(total_days))
    txt_file.write("\n")
    txt_file.write("Total Bike Users (08:00-16:00): " + str(total_bike_users_effective_hours))
    txt_file.write("\n")
    txt_file.write("Total Bike Users (Other Hours): " + str(total_bike_users_other_hours))
