# 3. Leap Year
# a. I/P -> Year, ensure it is a 4 digit number.
# b. Logic -> Determine if it is a Leap Year.
# c. O/P -> Print the year is a Leap Year or not.

def isLeapYear(year):
    if(year % 100==0 and year % 400==0):
        print(f"year {year} is a leap year")
    elif(year % 4 ==0 and year % 100 !=0):
        print(f"year {year} is a leap year")
    else:
        print(f"year {year} is not a leap year")

year=int(input("Enter the year : "))
isLeapYear(year)

