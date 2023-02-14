def pig_latin(word):
    """Pig latin to convert english words to pig latin

    Args:
        word (string): word to be translated
    """

    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'


try:
    word = str(input("enter a word to translate to pig latin: "))
except ValueError:
    print("Enter a string value: ")


print(pig_latin(word))
