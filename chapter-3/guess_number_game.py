import random

def guess_the_number(max_attempts=3):
    rand_num = random.randint(1, 100)

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"🔢 Attempt {attempt}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.\n")
            continue

        if guess == rand_num:
            print("\033[92m🎉 Congratulations! You guessed the correct number.\033[0m")
            break
        elif attempt < max_attempts:
            print("❌ Incorrect guess. Try again!\n")
        else:
            print("\033[91m💥 Game Over! The correct number was", rand_num, ".\033[0m")

# Run the game
guess_the_number()
