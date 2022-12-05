original_list = [1, 2, 4, 7, 8, 10]
print(f"List before reverse, {original_list}")

reverse_list = []
for value in original_list:
    reverse_list.insert(0,value)

print(f"List after reverse, {reverse_list}")