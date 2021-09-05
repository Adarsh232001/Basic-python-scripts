import datetime
user_input=input("Enter your goal and deadline in format:\ngoal:dealine(dd.mm.yyyy):-\n")
input_list=user_input.split(":")
goal = input_list[0]
deadline = input_list[1]
deadline_date=datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date=datetime.datetime.today()
#calculate how many days form now till deadline
time_till = deadline_date-today_date
print(f"Dear user! Time remainnig for your {goal} is {time_till}")