# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 

for n in student_scores:
    cont += 1
    maior = n
    if maior - student_scores[tamanho_lista - cont] > 0:
        maior = student_scores[tamanho_lista - cont]
    

        
print(maior)
   

        
    
    



