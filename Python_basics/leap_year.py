#WAP which takes an input form the user and check if the entered year is a leap year of not!
"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
"""




#First Way:
"""
number = int(input("Enter a year to check if it is leap year or not!"))

if (number%4 == 0):
  if(number%100 == 0):
    if(number%400 == 0):
      print("Leap Year")
    else:
      print("Not A Leap Year")
  else:
    print("Not A Leap Year")
  
else:
  print("Not A Leap Year")
"""




#Second Way:
def is_leap(year):
    leap = False
    if(year%4 == 0):
        if (year%100 !=0 or year%400 ==0):
            leap = True
    return leap
    
year = int(input("Enter a year to check if it is leap year or not!"))
print(is_leap(year))