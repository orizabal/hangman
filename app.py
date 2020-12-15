import random
import string
import inquirer

from words import words

play_again = [
    inquirer.List(
        'play_again',
        message='Would you like to play again?',
        choices=['Yes', 'No']
    )
]

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word or len(word) < 6:
        word = random.choice(words)

    return word.upper()

def print_hangman(attempt):
    if (attempt == 7):
        print("_________")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (attempt == 6):
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (attempt == 5):
        print( "_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (attempt == 4):
        print( "_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif (attempt == 3):
        print( "_________")
        print("|	 |")
        print("|	 O")
        print("|	\|")
        print("|	 |")
        print("|")
        print("|________")
    elif (attempt == 2):
        print( "_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|")
        print("|________")
    elif (attempt == 1):
        print( "_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")
    elif (attempt == 0):
        print( "_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")
        print("\n")

def hangman():
    word = get_valid_word(words)

    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()

    attempts = 7
    print_hangman(attempts)
    attempts -= 1
    
    print('\nLet\'s play hangman!')

    while len(letters) > 0 and attempts >= 0:
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
            else:
                print('\nThat guess was incorrect!\n')
                print_hangman(attempts)
                attempts -= 1
        elif user_guess in guessed_letters:
            print('\nYou\'ve already guessed this letter!\n')
        else:
            print('\nYou\'ve entered an invalid character. Please try again.\n')

    if len(letters) > 0:
        print('\nYou lose! The word was ',word)
    else:
        print('\nCorrect! The word is ',word)

    another_game = inquirer.prompt(play_again)
    if another_game['play_again'] == 'Yes':
        hangman()
    else:
        print('\nGoodbye!\n')

hangman()
