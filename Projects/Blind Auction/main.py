from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print('Wellcome to the secret auction program')
terminar = False
dic = {}
while not terminar == True:
  nome = input("What is your name? ")
  lance = int(input("What is your bid? $ "))
  outros = input("Are there any other bidders? Type 'yes' or 'no' \n")
  dic[nome] = lance
  if outros == 'yes':
    clear()
  else:
    terminar = True
    
maior = 0
vencedor = ''
for pessoa in dic:
   if dic[pessoa] > maior:
    maior = dic[pessoa]
    vencedor = pessoa
print(f"The winner is {vencedor}! with ${maior}!")
  
  
  
  


