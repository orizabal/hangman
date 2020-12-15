import random
import string

from words import words

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)

    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()

    while len(letters) > 0:
        # intro
        print('\nYou have guessed these letters: ', ' '.join(guessed_letters))

        letter_list = [letter if letter in guessed_letters else '-' for letter in word]
        print('\nWord: ', ' '.join(letter_list))

        # get user input
        user_guess = input('Guess a letter: ').upper()

        # add to set of guessed letters
        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)

            # if letter is in the word, remove from letters
            if user_guess in letters:
                letters.remove(user_guess)
        elif user_guess in guessed_letters:
            print('\nYou\'ve already guessed this letter!\n')
        else:
            print('\nYou\'ve entered an invalid character. Please try again.\n')

    print('\nCorrect! The word is ',word)

hangman()
