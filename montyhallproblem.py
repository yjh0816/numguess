from random import shuffle, choice

flag = False
s_count = 0
c_count = 0
# goat = 0, car = 1
doors = [
    0, 
    0, 
    1,
]

# Loop 200 cycle for calculating win rate each stay, change case
for i in range(1,200+1):
  shuffle(doors)
  # print(doors) 
  user_choice = choice(doors)
  # print(user_choice)

  # Except user's choice, check the goat door
  if user_choice == 0:
      c_count += 1
  else:
      s_count += 1

print("s_count:",s_count,"c_count:",c_count)
