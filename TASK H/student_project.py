import pandas as pd

data = {
    "Student_ID": [1,2,3,4,5,6,7,8,9,10],
    "Name": ["Ravi","Sneha","Amit","Neha","Rahul","Pooja","Arjun","Kiran","Meena","Suresh"],
    "Maths": [78,88,65,92,55,81,73,90,68,84],
    "Science": [85,90,70,89,60,79,76,88,72,82],
    "English": [80,86,60,94,58,85,70,91,65,86],
    "Attendance": [92,95,75,98,68,90,85,96,80,93]
}

df = pd.DataFrame(data)

# Save raw data
df.to_csv("students.csv", index=False)
# Step 2: Data Analysis
# Calculate average marks
df["Average_Marks"] = df[["Maths", "Science", "English"]].mean(axis=1)
# Top 3 students
top_students = df.sort_values(by="Average_Marks", ascending=False).head(3)
# Low performing students (avg < 60)
low_performers = df[df["Average_Marks"] < 60]
# Attendance vs performance
attendance_analysis = df[["Name", "Attendance", "Average_Marks"]]

# Step 3: Save final dataset
df.to_csv("students_final.csv", index=False)
# Step 4: Output results
print("Top 3 Performing Students:")
print(top_students[["Name", "Average_Marks"]])

print("\nLow Performing Students:")
print(low_performers[["Name", "Average_Marks"]])

print("\nAttendance vs Average Marks:")
print(attendance_analysis)
