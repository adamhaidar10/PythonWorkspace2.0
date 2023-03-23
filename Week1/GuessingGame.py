import random

random_number = random.randint(1, 100)
num_of_guesses = 0
user_guess = 0 

#print (random_number) take out when playing 

while user_guess != random_number:
    user_guess = int(input("Enter your guess: "))
    num_of_guesses += 1

    
    if user_guess > random_number:
            print ("Too high")
    elif user_guess < random_number:
            print ("Too low")

    else:
        print (f"You guessed correct in {num_of_guesses} tries!")