def list_reverse(original_list):
    if(len(original_list) == 0):
        return original_list
    else:
        return list_reverse(original_list[1: ]) + original_list[0]
    
original_list = [1,2,3,4,5,10]
print(f"List before reverse, {original_list}")

print(f"List after reverse, {list_reverse(original_list)}")