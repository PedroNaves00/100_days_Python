from art import logo
import random
def tentativas(dificuldade):
  if dificuldade == 'easy':
    return 10
  else:
    return 5
    
def adivinha(chance):
  if chance == numero:
    print(f"You got it!, the answer is {numero}")
    return chance 
  elif chance > numero:
    print("Too high")
    return chance
  else:
    print("Too low")
    return chance


print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100...")

numero = random.randint(1,100)
dificuldade = input("Choose a dificulty. Type 'easy' or 'hard': ")
parar = False
continuar = True
tentativas = tentativas(dificuldade)

while parar == False:
  tentativas -= 1
  print(f"You have {tentativas + 1} attempts.")
  chance = int(input("Make a guess: "))
  adivinha(chance)
  if tentativas == 0 and chance != numero:
    parar = True
    print("You've run out of guesses, you lose!")
  elif chance == numero:
    parar = True
  else:
    print("Guess again")