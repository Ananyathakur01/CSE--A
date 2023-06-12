name=input("Enter your name\n")
age=int(input("Enter your age\n"))
gender=input("Enter your Gender 'M' or 'F'\n")
days_worked=int(input("Enter your working days\n"))
if age >= 18 and age < 30:
    if gender == 'M':
        wages = 700 * days_worked
    elif gender == 'F':
        wages = 750 * days_worked
elif age >= 30 and age <= 40:
    if gender == 'M' or gender == 'F':
        wages = 800 * days_worked
print(f"{name} earned Rs {wages} for {days_worked} days of work.")
