def check_guess(guess,answer):
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct Answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1

    if attempt == 3:
        print('The correct answer is + ' + answer)


guess = input("Which one of these is a fish?\n \
        A) Whale\n B) Dolphon\n C)Shark\n D) Squid\n \
        Type A, B, C D ")

check_guess(guess, "C")
