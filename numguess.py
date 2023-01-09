from random import randint

# Generate random answer
answer = randint(1,100)

# Print answer
print("The answer is", answer)

# Get user name from user
username = input("Input your name: ")

# Say hello to user, using username
print("Nice to meet you, ",username)

# Get user guess from user
guess = int(input("Input your guess: "))

# Print guess
print("User's guess is", guess)
