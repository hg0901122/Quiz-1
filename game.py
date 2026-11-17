secret = 27
attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50. You have 5 attempts.")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    
    if guess == secret:
        print("You won!", secret, "is the correct number.")
        print()
        attempts = 0  # Stops the while loop when you win!
        
    elif guess > secret + 10: 
        print("Ice cold")
    elif guess < secret - 10:
        print("ice cold")
    elif guess > secret:
        print("Warm")
    else:
        print("Warm")

    if guess != secret:
        attempts = attempts - 1

        print("Remaining attemts: ", end="")
        for i in range(attempts):
            print("<3", end="")
        print()

if attempts == 0 and guess != secret:
    print("Game Over! The secret number was", secret)