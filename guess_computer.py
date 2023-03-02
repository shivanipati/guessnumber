
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low , high)

        else:
            guess= low

        feedback = input(f"is {guess} too high(h),too low(l),and too correct(c)")
        if feedback=='h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f"the correct guess number {guess}computer")

computer_guess(100)






