original_list = [1, 2, 3, 4, 5]
print("List before reverse : ", original_list)

list_reverse = []
for value in range(len(original_list)):
  list_reverse.append(original_list.pop())
  
print("List after reverse : ", list_reverse)
