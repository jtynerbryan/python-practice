import random

def rand_num():
    return random.randint(1, 10)

def eval_guess(num1,num2):
    if num1 > num2:
        print('Too low')
    else:
        print('Too high')

def game():
    num = rand_num()
    print('I\'m thinking of a number between 1 and 10')
    count = 3
    while count > 0:

        try:
            guess = int(input(f'What\'s the number? ({count} guesses remaining) '))
        except ValueError:
            print('That\'s not a number!')
            continue

        count -= 1
        if guess == num:
            print(f'That\'s right! The correct number is {num} ')
            break
        else:
            eval_guess(num, guess)

    play = input('Do you want to play again? y/n ')
    if play == 'y':
        game()
    else:
        return

game()
