original_list = [1, 2, 3, 4, 5]
slice_object = slice(None, None, -1)

list_reverse = original_list[slice_object]
print("List before reverse : ", original_list)

print("List after reverse : ", list_reverse)
