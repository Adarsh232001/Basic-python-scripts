import datetime
print("******************************Calculate your age***********************************")
birth=input("\nEnter your date of birth in dd-mm-yyyy hh:mm:ss :-")
birth_date = datetime.datetime.strptime(birth,"%d-%m-%Y %H:%M:%S")
print(birth_date)
todays_date = datetime.datetime.today()
age_in_days = todays_date - birth_date
#age_in_years = todays_date.year() - birth_date.year()
print(age_in_days)
#print(age_in_years)