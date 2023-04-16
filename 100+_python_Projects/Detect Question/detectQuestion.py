from nltk.tokenize import word_tokenize
question_words = ["what", "why", "when", "where",
                  "name", "is", "how", "do", "does",
                  "which", "are", "could", "would",
                  "should", "has", "have", "whom", "whose", "don't"]
question = input("Input a sentence: ")
question = question.lower()
question = word_tokenize(question)

# Check if question is in question words
if any(x in question[0] for x in question_words):
    print("This is a question!")
else:
    print("This is not a question!")
