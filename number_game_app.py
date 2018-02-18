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
    count = 0
    while True:
        guess = int(input('What\'s the number? '))
        count += 1
        if guess == num:
            print(f'That\'s right! The correct number is {num}')
            break
        else:
            eval_guess(num, guess)

    print(f'It took you {count} guesses to get the right number')

game()
