# Age Calculator Mini Project

from datetime import date

print("===== Age Calculator =====")

# Taking birth year, month, and day from user
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# Current date
today = date.today()

# Calculating age
age = today.year - birth_year

# Checking if birthday has occurred this year or not
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

# Displaying result
print("\nYour Age is:", age, "years")

# Extra information
print("Today's Date:", today)
print("Date of Birth:", birth_day, "/", birth_month, "/", birth_year)