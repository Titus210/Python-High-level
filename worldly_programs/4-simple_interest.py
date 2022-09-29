#!/usr/bin/python3
"""Find simple interest.
User chooses if to borrow or invest.
	Invest:
		simpple interest
		rate
		time(years)
	Borrow:
		rate
		amount to return
		time
"""
# choose either borrow or invest
def enter_choice(name):
	"""User chooses option which he wants to select"""
	action = int(input(f'Hello {name} \n 1. Invest amount\n 2. Borrow amount'))
	while True:
		if action == 1:
			invest_amount()
		elif action == 2:
			borrow_amount()
		else:
			print(f'Dear {name} please enter a valid option')


#-------------------------------
#         Invest
#-------------------------------

def invest_amount():
	principal = float(input("Enter amount you want to invest"))
	time = int(input("Enter time(months) you want to invest"))
	rate = 5
	print('The rate of investment is {:.2f} per month'.format((rate/100)))

# calculate simple interest

	simple_interest = (principal * (rate/100) * time)
	amount = simple_interest + principal
	
	print('Your total investment will sum to ksh.{:.2f} in {} months'.format(amount, time))
	print("Your rate is {1:.2f} for {0} months with an interest of {2:.2f} ".format(time, (rate/100), simple_interest))
	while True:
		try:
			option = int(input("Do you want to see money after each year?\n1. Yes \2. Quit"))
		except ValueError:
			print("Enter  valid number")
		break


#	print amount after time years

	if option == 1:
		i = 0
		while i < time:
			principal += principal * (rate/100)
			i += 1
			print('Month {} : {:.2f}'.format(i,principal))
	else:
		enter_choice(name)
#------------------------------
#        Borrow
#------------------------------

# calculate money to return

#calculate rate

#calculate time
print("Welcome user")
name = input("Please enter your name")
enter_choice(name)











