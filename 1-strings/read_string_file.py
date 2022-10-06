#!/usr/bin/python3
def main():
	with open ("name.txt",encoding = "utf-8") as f:
		counties = f.read().splitlines()
		print(f'The counties that are available are {counties}')
main()
