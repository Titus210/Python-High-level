from spellchecker import SpellChecker

corrector = SpellChecker()

word = input("Enter a word: ")
if word == corrector:
    print("This is a valid word")
else:
    correct_word = corrector.correction(word)
    print(f'The correct spelling of {word} is {correct_word}')

