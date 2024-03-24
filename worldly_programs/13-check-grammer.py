import nltk
from nltk.corpus import words

# Download NLTK word corpus
nltk.download('words')

# Set of English words
english_words = set(words.words())

def is_gibberish(word):
    # Criteria 1: If the word contains non-alphabetic characters
    if not word.isalpha():
        return True
    
    # Criteria 2: If the word is too short
    if len(word) <= 2:
        return True
    
    # Criteria 3: If the word is in all uppercase or all lowercase
    if word.isupper() or word.islower():
        return True
    
    # Criteria 4: If the word contains repetitive characters (e.g., 'aaa')
    if len(set(word.lower())) <= 2:
        return True
       
    return False

def check_sentence(sentence):
    words = sentence.split()
    gibberish_count = 0
    for word in words:
        if word.lower() not in english_words and is_gibberish(word):
            gibberish_count += 1
    
    # If more than half of the words are gibberish, classify the sentence as non-English
    if gibberish_count > len(words) / 2:
        return "Sorry, this is not an English sentence."
    else:
        return "Good sentence!"

sentence_to_check = input("Enter your sentence: ")
result = check_sentence(sentence_to_check)
print(result)