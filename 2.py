
birth_year = int(input("Enter the birth year: "))
birth_month = int(input("Enter the birth month (1-12): "))
birth_day = int(input("Enter the birth day of the month: "))


birth_date = datetime.datetime(birth_year, birth_month, birth_day)


day_of_week_index = birth_date.weekday()


days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_of_week = days_of_week[day_of_week_index]


print(f"The person was born on a {day_of_week}.")
