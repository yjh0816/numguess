from random import randint
from time import sleep

# Get user name from user
username = input("Input your name: ")

# Say hello to user, using username
print(f"Nice to meet you,{username}")

# Generate random answer
answer = randint(1,100)

# Print answer
print("The answer is", answer)

def compare_answer(guess):
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
        return True        
    elif guess > answer:
        print("The answer is lower than your guess")
    elif guess < answer:
        print("The answer is higher than your guess")
    else:
        print(f"Wrong answer. The answer is {answer}, {username}..")

# Get user guess from user
for i in range(5):
    num = int(input(f"So {username}, Guess the number(between 1~100): "))
    if compare_answer(num):
        break
