#!/usr/bin/python3
"""
	Calculating cost to operate server in a month
	Proomt user to enter amount to invest servers to host
	calculate days that invested amount can host servers entered
	 

"""
# Initializing  variables
cost_hour = 1.02
hours_day = 24
days_month = 30
no_server = float(input("Please Enter the amount of servers you want to host"))
money_invest =float(input("How much do you want to invest in dollars"))

# Calculating cost per month and per hour for one server
cost_day = cost_hour * hours_day
cost_month = cost_day * days_month

# Calculate cost per month and per day for users server
cost_day_server = no_server * cost_day
cost_month_server = cost_month * cost_day_server

## Budgeting 
days_hosted = money_invest / cost_day

		#Display Results
#	Print cost per day and month
print("Running a server will cost you \n ${0:.2f}: Per day \n ${1:.2f}: Per month".format(cost_day, cost_month))
print("Under your budget of ${0:.2f} Servers will run for ${1:.2f} days".format(money_invest, days_hosted))

