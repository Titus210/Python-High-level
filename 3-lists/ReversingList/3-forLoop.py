original_list = [1, 2, 4, 7, 8, 10]
print(f"List before reverse, {original_list}")
print(original_list)
reversed_list = []
for value in original_list:
    reversed_list = [value ] + reversed_list

print(reversed_list)
