from spellchecker import SpellChecker

corrector = SpellChecker()

while True:
    try:
        word = str(input("Enter a word: "))
    except ValueError:
        print("Please enter a valid word:")

    if word in corrector:
        print("This is a valid word")
        break
    else:
        correct_word = corrector.correction(word)
        print(f'The correct spelling of {word} is {correct_word}')
    break