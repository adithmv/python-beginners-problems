import random

secret = random.randint(1, 20)
tries = 0
max_tries = 5

print("Guess my number (1–20). You have 5 chances!")

while tries < max_tries:
    guess = int(input("Your guess: "))
    tries += 1

    if guess == secret:
        print(f"🎉 Correct! You found it in {tries} tries.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

if guess != secret:
    print(f"😢 Out of tries! The number was {secret}.")
