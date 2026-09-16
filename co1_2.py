import datetime

current_year = datetime.datetime.now().year

final_year = int(input("enter final year: "))

for year in range(current_year, final_year + 1):
    if year % 4==0:
        print(year)