# sort dictonary by value
def sortDict(dict):
    """Sort dictionary by value in asceding and descending order
    Args:
        dict(Dictionary): dictionary to sort"""

    # make dictonary values a list
    dict_list = list(dict.values())

    def descending(dict):
        """Sort dict in asceding order

        Args:
            dict (dictonary): list of dictonary to iterate
        """
        
        for i in range(len(dict)):
            for j in range(i+1, len(dict)):
                if dict_list[i] < dict_list[j]:
                    dict_list[i], dict_list[j] = dict_list[j], dict_list[i]
        return dict_list
    print(f"Dictonary in descending order \n {descending(dict)}")
            
    
    # ascending order
    def ascending(dict_list):
        """Reverse the list from previous descending order to attain ascending
        Args:
            dict_list(list): A list of  items to reverse"""
            
        reverse_list = []
        for value in dict_list:
            reverse_list = [value] + reverse_list
        print(f"Dictonary in ascending order \n {reverse_list}")

    ascending(dict_list)

dict = {
    "math": 82,
    "french": 88,
    "science": 55
}
sortDict(dict)
