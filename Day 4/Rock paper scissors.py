import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

jogada = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

lista = [rock, paper, scissors]
comp = random.choice(lista)


if jogada == "0":
  print(rock)
elif jogada == "1":
  print(paper)
elif jogada == "2":
  print(scissors)

print(f"Computer choose:{comp}")

if jogada == "0":
  if comp == rock:
    print("It's a draw")
  elif comp == paper:
    print("You lose")
  else:
    print("You win")
if jogada == "1":
  if comp == rock:
    print("You win")
  elif comp == paper:
    print("It's a draw")
  else:
    print("You lose")
if jogada == "2":
  if comp == rock:
    print("You lose")
  elif comp == paper:
    print("You win")
  else:
    print("It's a draw")

