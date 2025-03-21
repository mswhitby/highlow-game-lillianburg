import random
lower_bound = 1
upper_bound = 100
number_of_guesses = 0
random_number = random.randint(lower_bound,upper_bound)
guess = int(input("guess the number: "))
while guess != random_number: 
    if guess < random_number : print("the number is higher!")
else: print("the number is lower!")
number_of_guesses += 1
guess = int(input("guess the number: "))
print("congratulations! you guessed the number correctly in" , number_of_guesses,"attempts.")
