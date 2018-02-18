import random
# make a list of words
words = ['apple', 'banana', 'orange', 'coconut', 'strawberry', 'lime', 'grapefruit']
# pick a random word
# draw spaces
# take a guess
# draw guessed letters and strikes
# print out win or lose

while True:
    start = input('Press enter/return to start, press Q to end the game ')
    if start.lower() == 'q':
        break
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')

        print('')
        print(f'Strikes: {len(bad_guesses)}/7')
        print('')

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print('you can only guess a single letter')
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print('you\'ve already guessed that letter')
            continue
        elif not guess.isalpha():
            print('you can only guess letters')
            continue

        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(secret_word):
                print(f'you win! the word was {secret_word}')
                break
        else:
            bad_guesses.append(guess)



    else:
        print(f'you didn\'t guess the word. It was {secret_word}')
