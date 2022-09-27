#!/usr/bin/python3
details = {
	'fname':'Titus Kiplagat',
	"country": "Kenya",
	"region":"rift valley"}
print(f'USers details is {details}')
contact = {
	'Adress': 1212,
	'Zip': 2332,
	'Street': 'Kenyatta street'}
print(f'Contact infomation is {contact}')
detailed_contact = {**details, **contact}
print(f'Full details id {detailed_contact}')

