import time





def pig_latin(word):
    """Pig latin to convert english words to pig latin

    Args:
        word (string): word to be translated
    """

    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'


# get starting time to run the code
start_time = time.perf_counter()

try:
    word = str(input("enter a word to translate to pig latin: "))
except ValueError:
    print("Enter a string value: ")

print(pig_latin(word))

# get starting time to run the code
end_time = time.perf_counter()
time_taken = end_time - start_time

print(f"The total time taken is {time_taken:.2f} seconds")



