# Hangman

def get_word():
    while True:
        user_input = input('What word does the user have to guess?: ').upper()
        if not user_input.isalpha():
            print('Invalid input. Try again.\n')
        else:
            break
    return user_input


def get_lives():
    while True:
        try:
            user_input = int(input('How many lives does the player get?: '))
            if user_input <= 0:
                raise ValueError
        except ValueError:
            print('Invalid input. Try again.\n')
        else:
            break
    return user_input


def get_guess():
    while True:
        user_input = input('What letter would you like to guess?: ').upper()
        if not user_input.isalpha() or len(user_input) > 1:
            print('Invalid input. Try again.\n')
        else:
            break
    return user_input


def show_status(lives, mystery_word, guesses):
    print('The mystery word: ', end='')
    for letter in mystery_word:
        print(letter, end=' ')
    print()
    print(f'You have {lives} lives to guess the word correctly.')
    print('Wrong guesses: ', end='')
    for guess in guesses:
        print(guess, end=' ')
    print()


def main():
    print() # Adds newline after command line execution
    # Setup
    word = get_word()
    lives = get_lives()
    mystery_word = ['_'] * len(word)
    guesses = []
    over = False
    print('\n' * 15) # Attempts to hide the word that player has to guess

    while lives > 0 and not over:
        show_status(lives, mystery_word, guesses)
        guess = get_guess()
        if guess in word and guess not in mystery_word:
            for index, letter in enumerate(word):
                if letter == guess:
                    mystery_word[index] = letter
        elif guess in mystery_word or guess in guesses:
            print('You guessed that letter already. Try again.')
        else:
            if guess not in guesses:
                guesses.append(guess)
                guesses.sort()
            lives -= 1
        print()
        if ''.join(mystery_word) == word:
            over = True
        
    if lives == 0:
        print(f'You lost! The correct word was "{word}"\n')
    else:
        print(f'You guessed it right! The correct word was "{word}"\n')


if __name__ == '__main__':
    main()