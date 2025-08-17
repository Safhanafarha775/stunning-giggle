#AGE CALCULATOR

from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

# Take input from user
dob_input = input("Enter your Date of Birth in dd/mm/yyyy format: ")

# Split input and convert to integers
day, month, year = map(int, dob_input.split('/'))
dob = date(year, month, day)

print("Age =", calculate_age(dob))
