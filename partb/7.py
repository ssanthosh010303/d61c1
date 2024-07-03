# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
def is_leap_year(year):
    return True
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        else False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
