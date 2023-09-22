from datetime import date


def calculate_age(birth_year):
  today = date.today()
  age = today.year - birth_year
  return age


birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print("Your age is:", age)
