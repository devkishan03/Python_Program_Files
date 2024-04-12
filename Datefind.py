date=input("enter the date ex- dd/mm/yy :")
day=date[:date.find("/"):]
month=date[date.find("/")+1:date.rfind("/"):]
year=date[date.rfind("/")+1::]
print("date:",day)
print("month:",month)
print("year:",year)