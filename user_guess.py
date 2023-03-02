import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess= int(input(f"the guess number is 1 and {x}"))
        if guess< random_number:
            print("sorry guess again .low")

        elif guess>random_number:
            print("sorry guess again .high")

    print(f"hey you are correct guess number{random_number}correctly")


guess(10)