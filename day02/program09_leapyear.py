year=int(input("enter the year: "))
if year%4==0 and year%100!=100 and year%400==0:
    print("year is leap year which is: ",year)
else:
    print("year is not a leap year which is:",year)