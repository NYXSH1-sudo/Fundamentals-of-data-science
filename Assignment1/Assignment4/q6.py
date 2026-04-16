import pandas as pd # type: ignore

# Read the CSV file
df = pd.read_csv("health_data.csv")

print("Original DataFrame:")
print(df.head())
print(f"\nShape: {df.shape}")

#-Calculate BMI-
# BMI = Weight / Height
df['BMI'] = df['Weight'] / df['Height']
df['BMI'] = df['BMI'].round(2)  # Round to 2 decimal places

# --- Assign Health_Status based on BMI ---
def classify_health(bmi):
    '''Classify health status based on BMI value.'''
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy range"
    elif 25 <= bmi <= 29.9:
        return "Overweight risk"
    elif 30 <= bmi <= 34.9:
        return "High risk of diabetes/heart disease"
    else:
        return "Critical health condition"

df['Health_Status'] = df['BMI'].apply(classify_health)

# Display updated DataFrame
print("\nUpdated DataFrame with BMI and Health_Status columns:")
print(df.to_string(index=False))

# Summary of health status distribution
print("\nHealth Status Distribution:")
print(df['Health_Status'].value_counts())

# Save updated data to a new CSV
df.to_csv("health_data_with_bmi.csv", index=False)
print("\nUpdated data saved to 'health_data_with_bmi.csv'")