import random


# guess the number by the user
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Try again. Number is too low.")
        elif guess > random_number:
            print("Try again. Number is too high.")
    print(f"You guess correctly and the number is {guess}.")


# guess the number by the computer
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_number = random.randint(low, high)
        else:
            guess_number = low # this could be high as well, b/c low == high
        feedback = input(f'Is {guess_number} too high(H), too low(L), or correct(C)?? ').lower()
        if feedback == 'h':
            high = guess_number - 1
        elif feedback == 'l':
            low = guess_number + 1
    print(f"Yay!! the computer guessed your number, {guess_number} correctly.")


# test

# guess(10)
computer_guess(1000)
