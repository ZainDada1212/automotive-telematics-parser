import sqlite3
import pandas as pd

# 1. Load mock telematics data from the external CSV file
df = pd.read_csv('vehicle_logs.csv')
print("--- Raw Telematics Data Loaded from CSV ---")
print(df)

# 2. Filter for errors (Warnings or Offline statuses)
error_df = df[df['Device_Status'].isin(['Warning', 'Offline'])]
print("\n--- Filtered Protocol & Connection Errors ---")
print(error_df)

# 3. Store the filtered data into a local SQLite database
conn = sqlite3.connect('vehicle_telematics.db')
error_df.to_sql('error_logs', conn, if_exists='replace', index=False)
conn.close()
print("\n[Success] Filtered error logs saved to SQLite database (vehicle_telematics.db)!")

# 4. Connect back to the database and generate a summary report
conn = sqlite3.connect('vehicle_telematics.db')
report_df = pd.read_sql_query("SELECT Vehicle_ID, COUNT(*) as Error_Count, GROUP_CONCAT(Error_Code) as Errors FROM error_logs GROUP BY Vehicle_ID", conn)
conn.close()

print("\n==========================================")
print("   AUTOMATED VEHICLE TELEMATICS REPORT    ")
print("==========================================")
print(report_df)
print("==========================================")