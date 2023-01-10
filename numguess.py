from random import randint
from time import sleep

# Generate random answer
answer = randint(1,100)

# Print answer
print("The answer is", answer)

# Get user name from user
username = input("Input your name: ")

# Say hello to user, using username
print(f"Nice to meet you,{username}")

# Get user guess from user
guess = int(input(f"So {username}, Guess the number(between 1~100): "))

# Print user's guess
print(f"{username}'s guess is {guess}")

# Compare answer with user's guess
if guess == answer:
    print("******************")
    sleep(1)
    print("******************")
    sleep(1)
    print("******************")
    sleep(1)
    print(f"Collect! The answer is {answer}!!")
elif guess > answer:
    print("The answer is lower than your guess")
elif guess < answer:
    print("The answer is higher than your guess")
else:
    print(f"Wrong answer. The answer is {answer}, {username}..")
