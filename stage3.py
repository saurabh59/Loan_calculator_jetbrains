import math

print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal""")

k = input()
if k == "p":
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print("Enter the number of periods:")
    number_of_periods = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest / (12 * 100)
    loan_principal = annuity_payment / ((i * pow(1 + i, number_of_periods)) / (pow(i + 1, number_of_periods) - 1))
    print(f"Your loan principal = {loan_principal:.0f}!")

elif k == "n":
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    print("Enter the loan interest")
    interest = float(input())
    i = interest / (12 * 100)
    n = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))
    if n % 12 == 0:
        print(f"It will take {n // 12:.0f} years to repay the loan")
    else:
        print(f"It will take {(n // 12):.0f} years and {n % 12:.0f} months to repay the loan")
elif k == "a":
    print("Enter the loan principal:")
    loan_principal = float(input())
    print("Enter the number of periods:")
    number_of_periods = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest / (12 * 100)
    a = loan_principal * i * pow(1 + i, number_of_periods) / (pow(i + 1, number_of_periods) - 1)
    print(f"Your monthly payment = {math.ceil(a)}")
else:
    print("Invalid input. Please enter the valid input.")