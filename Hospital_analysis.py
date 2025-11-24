import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\samka\OneDrive\Documents\POWER BI DASHBAORD PROJECT\Hospital dataset.csv")
print(df.head())

# Count of patients per department using Bar Chart
dep_count= df["Department"].value_counts()
print("\n\nPatients per department:\n", dep_count)

plt.figure(figsize=(7,5))
dep_count.plot(kind="bar", color="Orange")
plt.title("Patients per Department")
plt.xlabel("Department")
plt.ylabel("Count of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Insurance Distribution among patients using Pie Chart
insurance_counts = df["Insurance"].value_counts()
print("\nNumber of Insurance based on Yes and No: \n", insurance_counts)

plt.figure(figsize=(6,6))
insurance_counts.plot(kind="pie", autopct="%1.1f%%", startangle =95,\
                      colors = ["gold", "lightblue"])
plt.title("Insurance Distrubution among Patients")
plt.ylabel("")
plt.show()

# Defining a function and creating a new column using that function, then
# making a Pie Chart of Age distribution into 3 categories
def age_group(a):
    if a<=18:
        return "Child"
    elif a <= 59:
        return "Adult"
    else:
        return "Senior"
    
df["Age_Group"] = df["Age"].apply(age_group)
print(df.groupby("Age_Group")["Age"].count())

age_group_counts = df["Age_Group"].value_counts()

plt.figure(figsize =(5,5))
age_group_counts.plot(kind="pie", autopct ="%1.1f%%", startangle =95,\
                      colors =["lightpink", "gold", "skyblue"])
plt.title("Age Group Distribution")
plt.ylabel("")
plt.show()

# Age Distribution using Histogram Chart
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=7, color="lightsalmon", edgecolor="black")
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Some analyzed Insights from the dataset:
# 1. Total patients
print("\nCount of total patients: ", len(df))

# 2. Common age groups
print("\nMost common age group of patients: ", df["Age_Group"].mode()[0])

# 3. Department with the highest number of patients
dep_high = df["Department"].value_counts().idxmax()
print(f"\nDepartment with the highest number of patients: {dep_high}")

# 4. Percentage of Insurance
insurance_percentage = (df["Insurance"].value_counts(normalize=True) * 100).round(2)
print(f"\nInsurance Coverage percentage: {insurance_percentage}%")

# 5. Avg treatment cost
avg_treatment_cost = df["TreatmentCost"].mean().round(2)
print("\nAverage Treatment Cost:", avg_treatment_cost)

# 6. Avg satisfaction score
avg_satisfaction = df["PatientSatisfaction"].mean().round(2)
print("\nAverage Satisfaction Score:", avg_satisfaction)



