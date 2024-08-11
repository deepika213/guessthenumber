import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0
    
    while True:
        guess = input("Take a guess: ")
        
        # Check if input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        number_of_guesses += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the right number in {number_of_guesses} tries.")
            break

    print("Thanks for playing!")

# Run the game
guessing_game()