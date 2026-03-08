import pandas as pd
import mysql.connector

# Read the correct CSV file
df = pd.read_csv("data/Heart_new2.csv")

# 🔍 Step 1: Check columns 
print("CSV Columns:", list(df.columns))
print("Total columns:", len(df.columns))
print("Total rows:", len(df))

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="heart_disease_db",
    auth_plugin="mysql_native_password"
)

cursor = conn.cursor()

# Create table if it doesn't exist based on CSV columns
create_table_sql = """
CREATE TABLE IF NOT EXISTS patients_heart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    heart_disease VARCHAR(10),
    bmi FLOAT,
    smoking VARCHAR(10),
    alcohol_drinking VARCHAR(10),
    stroke VARCHAR(10),
    physical_health INT,
    mental_health INT,
    diff_walking VARCHAR(10),
    sex VARCHAR(10),
    age_category VARCHAR(20),
    race VARCHAR(50),
    diabetic VARCHAR(50),
    physical_activity VARCHAR(10),
    gen_health VARCHAR(20),
    sleep_time FLOAT,
    asthma VARCHAR(10),
    kidney_disease VARCHAR(10),
    skin_cancer VARCHAR(10)
)
"""

cursor.execute(create_table_sql)

# Convert dataframe to list of tuples
data = df.values.tolist()

# Insert data
cursor.executemany("""
INSERT INTO patients_heart (
    heart_disease, bmi, smoking, alcohol_drinking, stroke,
    physical_health, mental_health, diff_walking, sex, age_category,
    race, diabetic, physical_activity, gen_health, sleep_time,
    asthma, kidney_disease, skin_cancer
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
""", data)

conn.commit()
conn.close()

print("✅ Data inserted successfully!")
print(f"✅ Inserted {len(df)} rows into patients_heart table")
