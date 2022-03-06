from itertools import count
import math
from tracemalloc import start

#account_one = 70% of contribution
#account_two = 30% of contribution

opening_balance = float(input("Enter opening balance of year:"))
dividend_rate = float(input("Enter dividend rate of year: ")) / 100
employee_contribution_rate = float(input("Enter employee contribution(%): ")) / 100
employer_contribution_rate = float(input("Enter employer contribution(%): ")) / 100

#when there are no changes to contribution rate and salary
def Constant_Year():
    opening_balance
    dividend_rate
    employee_contribution_rate
    employer_contribution_rate
    income = float(input("Enter salary: "))
    start_of_month = float(input("Enter start of month balance in Jan: "))
    list_of_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    employee_contribution = income * employee_contribution_rate
    employer_contribution = income * employer_contribution_rate
    
    counter = 0
    total_dividend = 0
    while (counter <= 11):
        end_of_month = start_of_month + employee_contribution + employer_contribution
        last_day = end_of_month * dividend_rate / 365
        start_of_month = end_of_month 
        if (counter == 0, 2, 4, 6, 7, 9, 11):
            first_to_second_last_day = start_of_month * dividend_rate / 365 * 31
            dividend_of_month = first_to_second_last_day + last_day
            total_dividend = total_dividend + dividend_of_month
            print("End of Month for ", list_of_months[counter], "is RM", end_of_month)
            print("Dividend for ", list_of_months[counter], " is RM", total_dividend)
            counter = counter + 1   
        elif (counter == 1):
            first_to_second_last_day = start_of_month * dividend_rate / 365 * 29
            dividend_of_month = first_to_second_last_day + last_day
            total_dividend = total_dividend + dividend_of_month
            print("End of Month for ", list_of_months[counter], "is RM", end_of_month)
            print("Dividend for ", list_of_months[counter], " is RM", total_dividend)
            counter = counter + 1
        else:
            first_to_second_last_day = start_of_month * dividend_rate / 365 * 30
            dividend_of_month = first_to_second_last_day + last_day
            total_dividend = total_dividend + dividend_of_month
            print("End of Month for ", list_of_months[counter], "is RM", end_of_month)
            print("Dividend for ", list_of_months[counter], " is RM", total_dividend)
            counter = counter + 1

def Account_One_Contribution():
    income = float(input("Enter salary: "))
    account_one = income * 0.7
    return account_one

def Account_Two_Contribution():
    income = float(input("Enter salary: "))
    account_two = income * 0.3
    return account_two

def January_Balance():
    # month_end = input("Enter end-of-January balance: ")
    # month_end = float(month_end)
    # after_dividend = month_end * dividend_rate
    # divided_balance = after_dividend / 365
    # jan_month_balance = divided_balance * 31
    jan_start_of_month = float(input("Enter start of month balance: "))
    income = float(input("Enter salary of month: "))
    employee_contribution = income * employee_contribution_rate
    employer_contribution = income * employer_contribution_rate
    jan_end_of_month = jan_start_of_month + employee_contribution + employer_contribution
    second_last_day = jan_start_of_month * dividend_rate / 365 * 30
    last_day = jan_end_of_month * dividend_rate / 365
    return jan_end_of_month
  
def February_Balance():
    # month_end = input("Enter end-of-February balance: ")
    # month_end = float(month_end)
    # after_dividend = month_end * dividend_rate
    # divided_balance = after_dividend / 365
    # feb_month_balance = divided_balance * 28
    # print(feb_month_balance)
    # return feb_month_balance
    feb_start_of_month = jan_end_of_month

def March_Balance():
    month_end = input("Enter end-of-March balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    mar_month_balance = divided_balance * 31
    print(mar_month_balance)
    return mar_month_balance

def April_Balance():
    month_end = input("Enter end-of-April balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    apr_month_balance = divided_balance * 30
    print(apr_month_balance)
    return apr_month_balance

def May_Balance():
    month_end = input("Enter end-of-May balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    may_month_balance = divided_balance * 31
    print(may_month_balance)
    return may_month_balance

def June_Balance():
    month_end = input("Enter end-of-June balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    june_month_balance = divided_balance * 30
    print(june_month_balance)
    return june_month_balance

def July_Balance():
    month_end = input("Enter end-of-July balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    july_month_balance = divided_balance * 31
    print(july_month_balance)
    return july_month_balance

def August_Balance():
    month_end = input("Enter end-of-August balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    aug_month_balance = divided_balance * 31
    print(aug_month_balance)
    return aug_month_balance

def September_Balance():
    month_end = input("Enter end-of-September balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    sep_month_balance = divided_balance * 30
    print(sep_month_balance)
    return sep_month_balance

def October_Balance():
    month_end = input("Enter end-of-October balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    oct_month_balance = divided_balance * 31
    print(oct_month_balance)
    return oct_month_balance

def November_Balance():
    month_end = input("Enter end-of-November balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    nov_month_balance = divided_balance * 30
    print(nov_month_balance)
    return nov_month_balance

def December_Balance():
    month_end = input("Enter end-of-April balance: ")
    month_end = float(month_end)
    after_dividend = month_end * dividend_rate
    divided_balance = after_dividend / 365
    dec_month_balance = divided_balance * 31
    print(dec_month_balance)
    return dec_month_balance

def True_Balance():
    sum_of_months = January_Balance + February_Balance + March_Balance + April_Balance + May_Balance + June_Balance + July_Balance + August_Balance + September_Balance + October_Balance + November_Balance + December_Balance
    print("Total Dividend of This Year is ", sum_of_months)

def main():
    # dividend_rate
    # January_Balance()
    # February_Balance()
    # March_Balance()
    # April_Balance()
    # May_Balance()
    # June_Balance()
    # July_Balance()
    # August_Balance()
    # September_Balance()
    # October_Balance()
    # November_Balance()
    # December_Balance()
    # True_Balance()
    Constant_Year()

if __name__ == "__main__":
    main()

