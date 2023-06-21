def interest_calculation(name, age, gender, principal, years):
    if gender == 'M':
        if age >= 60:
            rate= 0.12
        else:
            rate = 0.09 
    elif gender == 'F':       
        rate = 0.1
    else:
        rate = 0.09
          
    interest = principal * rate * years
    total_amount = principal + interest

    return interest, total_amount 

name = input("enter customer name: ")
age = int(input("enter customer age: ")) 
gender = input("enter customer gender(M/F): ")
principal = float(input("enter the principal anounmt:")) 
years = int(input("enter number of years: "))     

interest, total_amount =  interest_calculation(name, age, gender, principal, years)

print(f"customer name: {name}")
print(f"principal amount: {principal}")
print(f"interst amount {interest}")
print(f"total amount: {total_amount}")
