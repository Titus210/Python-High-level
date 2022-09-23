#!/usr/bin/python3
"""
	Program promts user to exter distance to travel
	if less than 3 miles advices user to walk
	If greater then 3 miles and less than 200 drive
	else if greater than 200 advices him to fly
"""
# Ask for distance

distance = float(input("Please enter distance you want to travel"))
## Determine  meaans of transport
if distance < 3:
	means = "walk"
	walk_message = "Walking is healthy and good for your body.Burn some few calories"
	print(walk_message)
elif distance < 200:
	means = "Drive"
	drive_message = " This is actually going to save your calories. Unless you want to burn out your calories while walking"
	print(drive_message)
else:
	means = "Fly"
	fly_message = "This would probably save the years you would have spent walking and your vehicle engine."
	print(fly_message)

#	Display method

print("I suggest you should {} to to your destination Have a safe journey ".format(means))
