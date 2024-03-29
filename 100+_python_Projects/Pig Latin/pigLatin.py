import time

""" If word begins with a vowel we add way to the end
if other letter we take first letter, put it on the end and add ay"""




def pigLatin():
    """Pig latin to convert english words to pig latin"""


    # get starting time to run the code
    start_time = time.perf_counter()
    
    begin_with_vowel = False

     # declarations
    word = str(input("Enter a word: "))
    vowels = ["a", "e", "i", "o", "u"]

    # check if word begins with vowel

    if word[0] in vowels:
            begin_with_vowel = True

    if begin_with_vowel == False:

        # get first word and remove it
        first_word = word[0]
        sliced_word = word.lstrip(first_word)
        word_ending = first_word + "ay" # add first word to ay

        new_word = sliced_word + word_ending    # create new word by adding first word with the ending created
        print(f"{word} begins with consonant and when added ay is {new_word}")  
    else:
        last_word = word + "way"

        print(f"{word} begins  with vowel and when added way is {last_word}")


    end_time = time.perf_counter()
    time_taken = end_time - start_time
    print(f"The total time taken is {time_taken:.2f} seconds")


pigLatin()
