#Homework1
name=input("Enter your name:")
user=int(input("Enter your age:"))
days=365*80
weeks=52*80
month=12*80
year=1*80
user_days=365*user
user_weeks=52*user
user_month=12*user
user_year=1*user
re_days=days-user_days
re_weeks=weeks-user_weeks
re_month=month-user_month
re_years=year-user_year

print(f"Hey {name} your remining Age :")
print(f"Year: {re_years}")
print(f"Months: {re_month}")
print(f"Weeks: {re_weeks}")  
print(f"Days: {re_days}")

.........................................................................
#Homework2
height=int(input("enter your height in cm:"))
age=int(input("enter your age:"))
bill=0
if height >= 120:
    if age < 18 and age >12 :
        print("your ticket price is RS.20")
        bill=20
    elif age >= 18:
        print("your ticket price is RS.50")
        bill=50
    elif age <12 :
        print("your ticket price is RS.10")
        bill=10
else:
    print("your height is less than 120cm")

want_photo=input("Do you want photo Y or N")
if want_photo=="Y" or "y":
    bill=bill+20
    print("Price of Photo is RS.20")
    print(f"Your bill is RS.{bill}")
else:
    print(f"Your bill is RS.{bill}")

