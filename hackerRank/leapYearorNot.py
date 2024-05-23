# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

year = int(input("enter year:"))

def checkyear(year):
    leap = False;
    remainder = year/4
    if remainder%2==0:
        leap = True
    return leap

print(checkyear(year))