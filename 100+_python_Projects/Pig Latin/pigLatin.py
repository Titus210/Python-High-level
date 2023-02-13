# If word begins with a vowel we add way to the end
# if other letter we take first letter, put it on the end and add ay


def pigLatin():
    """
    """

    begin_with_vowel = False

    word = str(input("Enter a word: "))
    vowels = ["a", "e", "i", "o", "u"]

    # check if word begins with vowel
    for vowel in vowels:
        if word[0] == vowel:
            begin_with_vowel = True

    if begin_with_vowel == False:
        # add way to end of word
        # get first word
        first_word = word[0]
        first_word_end = first_word + "ay"

        new_word = word + first_word_end
        print(f"{word} ends with and added way is {new_word}")
    else:
        last_word = word + "way"

        print(f"{word} ends with and added way is {last_word}")


pigLatin()
