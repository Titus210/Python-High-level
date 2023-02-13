# If word begins with a vowel we add way to the end
# if other letter we take first letter, put it on the end and add ay


def pigLatin():
    """
    """
    

    begin_with_vowel = False
    
    # enter word
    word = str(input("Enter a word: "))
    vowels = ["a","e","i","o","u"]
    
    for vowel in vowels:
        if word[0] == vowel:
            begin_with_vowel = True
    
    if  begin_with_vowel ==  False:
        print(f"{word} does not begin with vowel")
    else:
        print(f"{word} begins with vowel")
        
        

pigLatin()