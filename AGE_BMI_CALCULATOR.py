#Age related BMI Calculator

#AGE CALCULATOR

from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age
    
#calculating BMI
def calculate_bmi(h, w, age):
    h_in_m = float(h / 100)
    bmi = w / (h_in_m ** 2)   # correct formula

    # Check age group
    if age >= 20:
        # Adult BMI classification
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        elif 24.9 <= bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obese"
    else:
        # Children/teen BMI interpretation (simplified)
        if bmi < 5:
            status = "Underweight (percentile)"
        elif 5 <= bmi < 85:
            status = "Healthy (percentile)"
        elif 85 <= bmi < 95:
            status = "Overweight (percentile)"
        else:
            status = "Obese (percentile)"
    
    return bmi, status


# Taking inputs
weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in cms: "))

# Take dob from user
dob_input = input("Enter your Date of Birth in dd/mm/yyyy format: ")

# Split input and convert to integers
day, month, year = map(int, dob_input.split('/'))
dob = date(year, month, day)

age=calculate_age(dob)


bmi, status = calculate_bmi(height, weight, age)

print(f"\nYour BMI = {bmi:.2f}")
print(f"Status = {status}")