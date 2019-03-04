from math import tan, pi


def polysum(n,s):
	"""
	The function 'polysum' that takes 2 arguments, 'number of sides'(n) and 'length of Each sides'(s).
	This function sums the area and square of the perimeter of a regular polygon.
	The function returns the sum, rounded to 4 decimal places
	:param (n, s)
	:returns --> value of type float (round to 4 decimal places).
	"""

	area = (0.25*n*(s**2))/tan(pi/n)
	perimeter = n*s
	perimeter_squared = perimeter**2
	value = round(sum([area,perimeter_squared]),4)

	return value


def bal(
		balance = 42,
        annualInterestRate = 0.2,
        monthlyPaymentRate = 0.04
        ):
	prev_balance = balance

	# monthly 0
	Monthly_interest_rate= annualInterestRate / 12.0
	for i in range(12):
		Minimum_monthly_payment = monthlyPaymentRate * prev_balance

		Monthly_unpaid_balance = prev_balance - Minimum_monthly_payment

		Interest = Monthly_interest_rate * Monthly_unpaid_balance
		Updated_balance_each_month = Monthly_unpaid_balance + Interest
		prev_balance =Updated_balance_each_month

	return round(Updated_balance_each_month,2)



# prev_balance = balance
#
# # monthly 0
#
# Monthly_interest_rate= annualInterestRate / 12.0
# for i in range(12):
# 	Minimum_monthly_payment = monthlyPaymentRate * prev_balance
#
# 	Monthly_unpaid_balance = prev_balance - Minimum_monthly_payment
#
# 	Interest = Monthly_interest_rate * Monthly_unpaid_balance
# 	Updated_balance_each_month = Monthly_unpaid_balance + Interest
# 	prev_balance =Updated_balance_each_month
#
# print("Remaining balance: {}".format(round(Updated_balance_each_month, 2)))


def Lowest_payment(balance, annualInterestRate, Minimum_monthly_payment):
	Monthly_unpaid_balance = balance - Minimum_monthly_payment
	Monthly_interest_rate = annualInterestRate / 12.0
	for m in range(12):
		Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
		Monthly_unpaid_balance -= Minimum_monthly_payment
	return Updated_balance_each_month

balance = 3329
annualInterestRate = 0.2
MMPay = 10
newbalance = Lowest_payment(balance, annualInterestRate, MMPay)
while True:
	if newbalance <= 0:
		print('Lowest Payment: {}'.format(MMPay))
		break
	else:
		MMPay += 10
		newbalance = Lowest_payment(balance, annualInterestRate, MMPay)

# Paste your code into this box
def MIR(annualInterestRate):
    Monthly_interest_rate= (annualInterestRate) / 12.0
    return Monthly_interest_rate
def MMP(monthlyPaymentRate, balance):
    Minimum_monthly_payment = (monthlyPaymentRate) * (balance)
    return Minimum_monthly_payment
def MUB(balance,Minimum_monthly_payment):
    Monthly_unpaid_balance = (balance) - (Minimum_monthly_payment)
    return Monthly_unpaid_balance
def UBEM(Monthly_unpaid_balance,Monthly_interest_rate):
    Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
    return Updated_balance_each_month

def calbal(bal,anuIR):
    for i in range(12):
        Monthly_interest_rate = MIR(anuIR)
        Monthly_unpaid_balance = MUB(bal,MMPay)
        newbalance = UBEM(Monthly_unpaid_balance,Monthly_interest_rate)
    return newbalance


MMPay = 10
newbalance = balance
while True:
    newbalance = calbal(newbalance,annualInterestRate)
    if newbalance < 0:
        print('Lowest Payment: {}'.format(MMPay))
        break
    else:
        newbalance = balance
        MMPay += 10