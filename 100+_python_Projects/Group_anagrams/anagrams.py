from collections import defaultdict


def group_anagrams(word):
    """Function to group anagrams
            :param word: list of  words to group
             return: grouped anagrams
    """
    default_dict = defaultdict(list)
    for letter in word:
        sorted_words = " ".join(sorted(letter))
        default_dict[sorted_words].append(letter)

    return default_dict.values()


class Anagrams:
    def group_anagrams(self, words):
        """Function to group anagrams
            : param word: list of  words to group
            return: grouped anagrams
        """
        dictonary = {}
        for word in words:
            sorted_word = "".join(sorted(word))
            # Check if the word is already in the dictionary
            if sorted_word not in dictonary:
                dictonary[sorted_word] = [word]

            # if present means that the word ia an anagram
            else:
                dictonary[sorted_word] += [word]
        return [dictonary[i] for i in dictonary]


def main():
    while True:
        try:
            no_words = int(input('Enter number of words to enter: '))
        except ValueError:
            print("Please enter a valid number")
        if no_words < 2:
            print("Please Number of words can't be less than two")
            main()
        else:
            words = []
            for i in range(no_words):
                try:
                    word = str(input("Please enter a word to check anagram: "))
                    words.append(word)
                except ValueError:
                    print("Please enter a valid string")
        break

    # calling function
    print(group_anagrams(words))

    # calling class function
    if __name__ == "__main__":
        print(Anagrams().group_anagrams(words))


main()
