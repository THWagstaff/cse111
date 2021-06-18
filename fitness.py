from datetime import datetime

def main():
  gender = input('What is your Gender? (M/F) ')
  birth_date = input('What is your birth date? (YYYY-MM-DD) ')
  pounds_weight = float(input('How much do you weigh in US Pounds? '))
  height = float(input('How tall are you in US inches? '))
  
  age = compute_age(birth_date)

  kg = kg_from_lb(pounds_weight)

  cm = cm_from_in(height)

  bmi = body_mass_index(kg, cm)

  bmr = basal_metabolic_rate(gender, kg, cm, age)

  print(f"Age(years): {age}")
  print(f"Weight(kg): {kg:.2f}")
  print(f"Height(cm): {cm:.1f}")
  print(f"Body Mass index: {bmi:.1f}")
  print(f"Basal Metabolic Rate (kcal/day): {bmr:.0f}")
  


def compute_age(birth):
  birthday = datetime.strptime(birth, "%Y-%m-%d")
  today = datetime.now()

  # Compute the difference between today and the birthday in years.
  years = today.year - birthday.year

  # If necessary, subtract one from the difference.
  if birthday.month > today.month or \
    (birthday.month == today.month and birthday.day > today.day):
    years -= 1
  return years
  

def kg_from_lb(lb):
  kilograms = lb/2.2046
  
  return kilograms

def cm_from_in(inch):
 
 cm = inch * 2.54

 return cm



def body_mass_index(weight, height):
  
  bmi = 10000 * weight / (height ** 2)
  return bmi

def basal_metabolic_rate(gender, weight, height, age):
  if gender == "F":
   bmr = 447.593 + 9.247 * weight + 3.098*height - 4.330 * age
  elif gender == "M":
   bmr = 88.362 + 13.397 * weight + 4.799*height - 5.677 * age
  else:
    print('Hey you did not use a correct variable. Please try again' )
  return bmr

main()

