#!/usr/bin/python3
"""
	Calculating cost to operate server in a month
	Steps:
		Cost per hour = $1.02
		hours per day = 24
		days in a month = 30
		cost per day = cost per hour * hours per day
		cost per month = cost per day * 30
"""
cost_hour = 1.02
hours_day = 24
days_month = 30
cost_day = cost_hour * hours_day
cost_month = cost_day * days_month
#	Print cost per day and month
print("Running a server will cost you {} per day and {} per month".format(cost_day, cost_month))
