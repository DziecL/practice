import math
import argparse


def f_annuity(payment, principal, periods, interest):
    months = periods
    if payment is not None:
        payment = int(payment)
    if principal is not None:
        principal = int(principal)
    if interest is not None:
        interest = float(interest)

    if months is None:
        i = (float(interest) / 100) / 12
        a = float(payment) / (float(payment) - i * float(principal))
        b = 1 + float(i)

        months = math.log((float(a)), float(b))
        months = math.ceil(months)
        yr = math.floor(months / 12)
        mth = months % 12

        if mth == 0:
            print('It will take', yr, 'years' if yr > 1 else 'year', 'to repay this loan!')
        elif yr == 0:
            print('It will take', mth, 'months' if mth > 1 else 'month', 'to repay this loan!')
        else:
            print('It will take', yr, 'years' if yr > 1 else 'year', 'and',
                  mth, 'months' if mth > 1 else 'month ', 'to repay this loan!')

        print('Overpayment =', round(int(payment) * int(months) - int(principal)))

    elif payment is None:

        i = (float(interest) / 100) / 12

        payment = float(principal) * ((i * math.pow(1 + i, float(months))) / (math.pow(1 + i, float(months)) - 1))

        print('Your monthly payment =', str(math.ceil(payment)) + '!')
        print('Overpayment =', round(math.ceil(payment) * int(months) - int(principal)))

    elif principal is None:
        i = (float(interest) / 100) / 12

        principal = float(payment) / ((i * math.pow(1 + i, float(months))) / (math.pow(1 + i, float(months)) - 1))

        print('Your loan principal = ', str(round(principal)) + '!')
        print('Overpayment =', round(int(payment) * int(months) - int(principal)))
    else:
        print('wtf')


def f_diff(principal, periods, interest):
    months = int(periods)
    principal = int(principal)
    i = (float(interest) / 100) / 12

    m = 1
    full = 0

    while m <= months:
        diff = math.ceil(principal/months + i * (principal - (principal * (m - 1)/months)))
        print('Month', str(m) + ':', 'payment is', diff)
        full += diff
        m += 1

    print('Overpayment =', round(round(full) - int(principal)))


parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

check = [args.payment, args.principal, args.periods, args.interest]
j = 0

for i in range(len(check)):
    if check[i] is None:
        j += 1
    elif float(check[i]) < 0:
        print('Incorrect parameters.')
        exit(0)

if j > 1 or args.interest is None:
    print('Incorrect parameters.')
    exit(0)


if args.type == "annuity":
    f_annuity(args.payment, args.principal, args.periods, args.interest)
elif args.type == "diff":
    f_diff(args.principal, args.periods, args.interest)



