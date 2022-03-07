# how the equation works
# a = balance on the 1st of each month
# b = number of days in the month
# c = contribution amount for the month account 1
# d = one day
# aggregate balance = (a x b) + (c x d)
# true equation = aggregate balance * dividend rate / number of days in year

def leap_year_check(year):
    if (year % 4 == 0) and (year % 100 != 0):
        leap_year_check.days_of_year = 366
    else:
        leap_year_check.days_of_year = 365

year = int(input("Enter the year:"))
leap_year_check(year)

salary = float(input("Enter your salary: "))
dividend_rate = float(input("Enter dividend rate of the year: ")) / 100
employee_contribution = float(input("Enter your contribution (%): ")) / 100
employer_contribution = float(input("Enter employer contribution (%): ")) / 100
opening_balance = float(input("Enter opening balance of year: "))
contribution_of_month = salary * (employee_contribution + employer_contribution)
constant = 1
list_of_months = list_of_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# for adding up monthly
first_of_jan = opening_balance
total_dividend = 0

counter = 0
while (counter <= 11):
    if (counter == 0, 2, 4, 6, 7, 9, 11):
        days = 31
        aggregate_balance = (first_of_jan * days) + (contribution_of_month * constant)
        calculation_equation = (aggregate_balance * dividend_rate) / leap_year_check.days_of_year
        print("Dividend is RM", calculation_equation, "in", list_of_months[counter])
        first_of_following_month = first_of_jan + contribution_of_month
        first_of_jan = first_of_following_month
        counter = counter + 1
    
    elif (counter == 1):
        days = 28
        aggregate_balance = (first_of_jan * days) + (contribution_of_month * constant)
        calculation_equation = (aggregate_balance * dividend_rate) / leap_year_check.days_of_year
        print("Dividend is RM", calculation_equation, "in", list_of_months[counter])
        first_of_following_month = first_of_jan + contribution_of_month
        first_of_jan = first_of_following_month
        counter = counter + 1
    
    else:
        days = 30
        aggregate_balance = (first_of_jan * days) + (contribution_of_month * constant)
        calculation_equation = (aggregate_balance * dividend_rate) / leap_year_check.days_of_year
        print("Dividend is RM", calculation_equation, "in", list_of_months[counter])
        first_of_following_month = first_of_jan + contribution_of_month
        first_of_jan = first_of_following_month
        counter = counter + 1

    
    total_dividend = total_dividend + calculation_equation
    rounded_value = round(total_dividend, 2)
    total_amount = rounded_value + first_of_following_month

print("Total dividend is RM", rounded_value)
print("Total accounts balance is RM", first_of_following_month)
print("Total amount after dividend at end of", year, "is RM", total_amount)
