import argparse
import math
parser = argparse.ArgumentParser(description="It is a loan calculator")
parser.add_argument("-t", "--type", choices=["annuity", "diff"], help="Incorrect parameters")
parser.add_argument("-p", "--payment", type=int)
parser.add_argument("-i", "--interest", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--principal", type=int)
args = parser.parse_args()
if args.interest:
    if args.type == "diff":
        if args.payment:
            print("Invalid parameters")
        elif args.principal and args.periods:
            if args.principal > 0 and args.periods > 0 and args.interest > 0:
                i = args.interest / (12 * 100)
                p = args.principal
                n = args.periods
                total = 0
                for m in range(1, args.periods + 1):
                    amount = p / n + i * (p - p * (m - 1) / n)
                    total += math.ceil(amount)
                    print(f"Month {m}: payment is {math.ceil(amount)}")
                print()
                print(f"Overpayment = {total - p}")
            else:
                print("Incorect parameters")
        else:
            print("Invalid parameters")
    else:
        if args.payment and args.principal:
            if args.payment > 0 and args.principal > 0:
                a = args.payment
                p = args.principal
                i = args.interest / 1200
                n = math.ceil(math.log(a / (a - i * p), i + 1))
                if n % 12 == 0:
                    print(f"It will take {n // 12:.0f} years to repay the loan")
                else:
                    print(f"It will take {(n // 12):.0f} years and {n % 12:.0f} months to repay the loan")
                print(f"Overpayment = {n * a - p}")
            else:
                print("Incorrect parameters")
        elif args.periods and args.payment:
            if args.periods > 0 and args.payment > 0:
                n = args.periods
                p = args.payment
                i = args.interest / 1200
                principal_loan = math.ceil(p / ((i * pow(i + 1, n)) / (pow(i + 1, n) - 1)))
                print(f"Your loan principal = {principal_loan}!")
                print(f"Overpayment = {n * p - principal_loan}")
            else:
                print("Incorrect parameters")
        elif args.periods and args.principal:
            if args.periods > 0 and args.principal > 0:
                p = args.principal
                n = args.periods
                i = args.interest / 1200
                a = math.ceil((p * pow(i + 1, n) * i) / (pow(i + 1, n) - 1))
                print(f"Your monthly payment = {a}!")
                print(f"Overpayment = {n * a - p}")
        else:
            print("Incorrect parameters")
else:
    print("Incorrect parameters")