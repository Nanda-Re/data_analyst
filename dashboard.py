import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load data from hourly analysis file
try:
    hourly_data = pd.read_csv("bike_analysis.txt", sep=",", skiprows=2)
    if hourly_data is None:
        raise ValueError("Data is None. Please check the format/content of bike_analysis.txt.")
    
    # Print the loaded data for debugging
    st.write("Hourly Data:")
    st.write(hourly_data)

    if "Days" in hourly_data.columns and "Effective Hours" in hourly_data.columns and "Other Hours" in hourly_data.columns:
        total_days_hour = hourly_data["Days"].iloc[0]
        total_bike_users_effective_hours = hourly_data["Effective Hours"].iloc[0]
        total_bike_users_other_hours = hourly_data["Other Hours"].iloc[0]

        # Chart for Hourly Data
        st.subheader("Hourly Data Chart")
        fig_hourly, ax_hourly = plt.subplots()
        hourly_data.plot(x='Days', y=['Effective Hours', 'Other Hours'], kind='bar', ax=ax_hourly)
        ax_hourly.set_xlabel('Days')
        ax_hourly.set_ylabel('Hours')
        st.pyplot(fig_hourly)
        
    else:
        ValueError=False    

except pd.errors.ParserError as e:
    st.error(f"Error reading bike_analysis.txt: {e}")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while processing bike_analysis.txt: {e}")
    st.stop()

# Load data from daily analysis file
try:
    daily_data = pd.read_csv("analisis_penggunaan.txt", sep=",", skiprows=1)
    if daily_data is None:
        raise ValueError("Data is None. Please check the format/content of analisis_penggunaan.txt.")
    
    # Print the loaded data for debugging
    st.write("Daily Data:")
    st.write(daily_data)

    if "actual_column_name_1" in daily_data.columns and "actual_column_name_2" in daily_data.columns and "actual_column_name_3" in daily_data.columns:
        total_days_day = daily_data["actual_column_name_1"].iloc[0]
        total_users = daily_data["actual_column_name_2"].iloc[0]
        avg_users_per_day = daily_data["actual_column_name_3"].iloc[0]
        avg_users_weekday = daily_data["actual_column_name_4"].iloc[0]
        avg_users_weekend = daily_data["actual_column_name_5"].iloc[0]
    else:
        ValueError=False
except pd.errors.ParserError as e:
    st.error(f"Error reading analisis_penggunaan.txt: {e}")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while processing analisis_penggunaan.txt: {e}")
    st.stop()


# Chart for Daily Data
st.subheader("Daily Data Chart")
fig_daily, ax_daily = plt.subplots()
daily_data.plot(x='Total Hari', y=['Rata-rata Pengguna per Hari', 'Rata-rata Pengguna pada Hari Kerja', 'Rata-rata Pengguna pada Akhir Pekan'], kind='bar', ax=ax_daily)
ax_daily.set_xlabel('Total hari') 
ax_daily.set_ylabel('Total Pengguna') 
st.pyplot(fig_daily)


