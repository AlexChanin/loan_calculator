# write your code here
from math import ceil
from math import floor
from math import log
import argparse


parser = argparse.ArgumentParser(description="""
This program is a loan calculator.
For differentiated payments (provide type="diff"):
To calculate differentiated payments specify the following parameters:
loan principal (int), 
loan interest (float wo %-sign), 
period of monthly payments (int).
For annuity payments (provide type="annuity"):
1. To calculate the annuity payment for a loan specify the following parameters:
loan principal (int), 
loan interest (float wo %-sign), 
period of monthly payments (int).
2. To calculate the principal with annuity payments specify the following parameters: 
annuity monthly payment (int), 
loan interest (float wo %-sign), 
period of monthly payments (int).
3. To calculate how long period of monthly payments specify the following parameters:
loan principal (int), 
loan interest (float wo %-sign), 
annuity monthly payment (int)""")

parser.add_argument("--type", choices=["annuity", "diff"],
                    help='Specify type of payment: "annuity" or "diff" (differentiated).')
parser.add_argument("--interest", type=float, help='Specify the loan interest (float).')
parser.add_argument("--principal", type=int, help='Specify the loan principal (int).')
parser.add_argument("--payment", type=int, help='Specify the monthly payment amount (int).')
parser.add_argument("--periods", type=int, help='Specify the number of months (int).')

args = parser.parse_args()
parameters = [args.type, args.interest, args.principal, args.payment, args.periods]

if args.type is None:
    print("Incorrect parameters.")
elif len([x for x in parameters[1:] if x is not None and x < 0]) != 0:
    print("Incorrect parameters.")
elif args.type == "diff":
    if args.payment is None and args.interest is not None and \
            args.principal is not None and args.periods is not None:
        nominal_monthly_interest_rate = args.interest / (12 * 100)
        overpayment = 0
        for m in range(1, args.periods+1):
            differentiated_payment =  \
                ceil(args.principal / args.periods + nominal_monthly_interest_rate *
                     (args.principal - args.principal * (m - 1) / args.periods))
            overpayment += differentiated_payment
            print(f"Month {m}: payment is {differentiated_payment}")
        overpayment -= args.principal
        print(f"\nOverpayment = {overpayment}")
    else:
        print("Incorrect parameters.")
else:
    if args.payment is not None and args.interest is not None and \
            args.principal is not None and args.periods is None:
        nominal_monthly_interest_rate = args.interest / (12 * 100)
        number_of_months = \
            ceil(log(
                    args.payment /
                    (args.payment - nominal_monthly_interest_rate * args.principal),
                    1+nominal_monthly_interest_rate))
        if number_of_months // 12 == 1:
            suffix_y = ""
        else:
            suffix_y = "s"
        if number_of_months == 1 or number_of_months % 12 == 1:
            suffix = ""
        else:
            suffix = "s"
        if number_of_months // 12 == 0:
            print(f"It will take {number_of_months} month{suffix} to repay this loan!")
        elif number_of_months % 12 == 0:
            print(f"It will take {number_of_months // 12} year{suffix_y} to repay this loan!")
        else:
            print(f"It will take {number_of_months // 12}",
                  f"year{suffix_y} and {number_of_months % 12} month{suffix} to repay this loan!")
        overpayment = number_of_months * args.payment - args.principal
        print(f"Overpayment = {overpayment}")
    elif args.payment is None and args.interest is not None and \
            args.principal is not None and args.periods is not None:
        nominal_monthly_interest_rate = args.interest / (12 * 100)
        annuity_payment = \
            ceil(args.principal * (nominal_monthly_interest_rate *
                                   (1 + nominal_monthly_interest_rate) ** args.periods /
                                   ((1 + nominal_monthly_interest_rate) ** args.periods - 1)))
        print(f"Your monthly payment = {annuity_payment}!")
        overpayment = annuity_payment * args.periods - args.principal
        print(f"Overpayment = {overpayment}")
    elif args.payment is not None and args.interest is not None and \
            args.principal is None and args.periods is not None:
        nominal_monthly_interest_rate = args.interest / (12 * 100)
        loan_principal = \
            floor(args.payment / (nominal_monthly_interest_rate *
                                  (1 + nominal_monthly_interest_rate) ** args.periods /
                                  ((1 + nominal_monthly_interest_rate) ** args.periods - 1)))
        print(f"Your loan principal = {loan_principal}!")
        overpayment = args.payment * args.periods - loan_principal
        print(f"Overpayment = {overpayment}")
    else:
        print("Incorrect parameters.")
