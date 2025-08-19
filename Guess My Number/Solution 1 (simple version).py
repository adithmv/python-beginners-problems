import random

# computer chooses a number
secret = random.randint(1, 20)

tries = 0
guess = 0

print("I'm thinking of a number between 1 and 20...")

while guess != secret:
    guess = int(input("Take a guess: "))
    tries += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! 🎉 You guessed it in {tries} tries.")
