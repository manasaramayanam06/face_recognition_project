import pandas as pd

# Load your Excel file
df = pd.read_excel("attendance.xlsx", header=None)

# Add proper column names to match your current data
df.columns = ["RawName", "RawDateTime", "Status"]

# --- Clean Name ---
# Remove ".jpg" if present
df["Name"] = df["RawName"].astype(str).str.replace(".jpg", "", regex=False)

# --- Split Date & Time ---
# Convert RawDateTime to datetime if possible
df["RawDateTime"] = pd.to_datetime(df["RawDateTime"], errors="coerce")

# Extract date and time separately
df["Date"] = df["RawDateTime"].dt.date
df["Time"] = df["RawDateTime"].dt.time

# --- Final Clean Format ---
final_df = df[["Name", "Date", "Time", "Status"]]

# Save to new Excel file
final_df.to_excel("formatted_attendance.xlsx", index=False)

print("✅ Attendance file formatted successfully! Check 'formatted_attendance.xlsx'")
