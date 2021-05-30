print("Enter the credit principal")
principal = int(input())
print("""What do you want to calculate?
type "m" for the number of months,
type "p" for the monthly payment""")

k = input()
if k == "p":
    months = int(input("Enter the number of months:"))
    if principal % months == 0:
        print(f"Your monthly payment = {principal / months}")
    else:
        payment = round((principal / months) + 0.5)
        last_payment = principal - (months - 1) * payment
        print(f"Your monthly payment = {payment} with last monthly payment = {last_payment}.")
elif k == "m":
    print("Enter the monthly payment:")
    monthly = int(input())
    number = principal / monthly
    if number == 1:
        print("It takes 1 month to repay the credit")
    else:
        print(f"It takes {number} months to repay the credit")

