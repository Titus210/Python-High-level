#/usr/bin/python3
empNames = ['',]
while True:
	name = input("Enter names of employees")
	if name == ' ':
		break
	empNames.append(name)
	print('The cat names are:')
print('The employee names are')
for i in empNames:
	print('  ' + name)
