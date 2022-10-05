#!/usr/bin/python3
def minMAx_avg(*tupple):
	"""Iterates in loops and checks if number is large"""
	# Initialize max avg and min
	for i in tupple:
		global maximum = len(i)
		global avg = 0
		global minimum = 0
		if len(i) > maximum:
			maximum = i
		elif len(i) >= avg:
			avg = i
		else:
			minimum = i
	return maximum , minimum , avg
avg = minMAx_avg(["Titus","Selly", "cliche", "ok"])
print(f'Maximum is {int(maximum)} \n average is {int(avg)} \n minimum  is  {int(minimum)}')
